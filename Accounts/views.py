from django.conf import settings
from django.http import request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView,GenericAPIView,ListAPIView
from rest_framework.views import APIView
from .serializers import UsersSerializer,LoginSerializer
from .models import Users,Account,Invite
from django.contrib.auth import authenticate,login
from .twilio import send_sms,checking
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

class RegisterationView(CreateAPIView):

    serializer_class = UsersSerializer

    def post(self, request, *args, **kwargs):

        company_detail=Account.objects.filter(role="Super Admin",company_name=request.data['company_name'])

        if company_detail:
            return Response({'message':"company already Exited"},status=status.HTTP_208_ALREADY_REPORTED)
        else:
            if Users.objects.filter(email=request.data['email']):
                return Response({'message':'Email already Exist'},status=status.HTTP_208_ALREADY_REPORTED)
            if Users.objects.filter(mobile_number=request.data['mobile_number']):
                return Response({'message':'Mobile number already Exist'},status=status.HTTP_208_ALREADY_REPORTED)
            role = Account.objects.create(role="Super Admin",company_name=request.data['company_name'])
            update_request = request.data.copy()
            update_request.update({'role':role.pk})
            serializer = self.get_serializer(data=update_request)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('success')


class LoginView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self,request):

        email = request.data.get('email')
        password = request.data.get('password')
        if Users.objects.filter(email=email).first():
            user = authenticate(email=email,password=password)

            if user is None:
                return Response({'message':'invalid Credential'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message':'Invalid email'},status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class OtpLoginView(APIView):


    def post(self,request):

        mobile_number = request.data['mobile_number']
        user = Users.objects.filter(mobile_number=mobile_number[3:]).first()
        if user:
            try:
                send_sms(mobile_number)
                return Response({"message":"success"},status=status.HTTP_200_OK)
            except:
                return Response({"message":"connection problem pls try again later"},status=status.HTTP_408_REQUEST_TIMEOUT)
            
        
        return Response({'user is not found'},status=status.HTTP_404_NOT_FOUND)

class OtpCheckView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self,request):

        mobile_number = request.data['mobile_number']
        otp = request.data['otp']
        user = Users.objects.filter(mobile_number=mobile_number[3:]).first()
        if user:
            try:
                if checking(mobile_number,otp) == 'approved':
                    login(request,user)
                    serializer = self.serializer_class(user)
                    return Response(serializer.data)

                return Response({"message":"invalid otp"},status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response({"message":"otp expires or already used "},status=status.HTTP_401_UNAUTHORIZED)
                
        return Response({"message":"invalid mobile number"},status=status.HTTP_401_UNAUTHORIZED)



class InvitationView(APIView):

    def post(self,request):
        mail = request.data['email']
        role_instance = Account.objects.filter(role=request.data['role'],company_name = "brototype").first()
        if role_instance:
            role = role_instance
        else:
            role = Account.objects.create(role=request.data['role'],company_name = "brototype")

        
        already_existed_mails =""
        email = mail.split(',')
        for i in email:
            if Invite.objects.filter(email=i).first() or Users.objects.filter(email = i).first():
                already_existed_mails = already_existed_mails +(i + ",")
            else:
                Invite.objects.create(email=i,role=role)
                subject = 'WELCOME TO CRM'
                text_content= (f"hi welcome {i}")
                html_content = render_to_string('invite.html',{"team" : "Brototype"})
                to_email = i
                send_email = EmailMultiAlternatives(subject,text_content,settings.EMAIL_HOST_USER,[to_email])
                send_email.attach_alternative(html_content,"text/html")
                send_email.send()
        if already_existed_mails:
            return Response({'message':"invitation is already send to these emails",'emails':already_existed_mails},status=status.HTTP_208_ALREADY_REPORTED)
        return Response('success')


class TeamSignUpView(APIView):
    

    def post(self,request):
        email = request.data['email']
        invited_member = Invite.objects.filter(email=email).first()

        if invited_member:
            role = invited_member.role
            invited_member.delete()
        else:
            return Response({'message': "invalid email id, check your email id , enter provided email id or alredy registered "},status=status.HTTP_404_NOT_FOUND)
        name = request.data['name']
        mobile_number = request.data['mobile_number']
        user_instance = Users.objects.create(email=email,mobile_number=mobile_number,name=name,role=role)
        if role.role == 'Admin':
            user_instance.is_admin = True
            user_instance.is_staff = True
        else:
            user_instance.is_staff = True
        user_instance.save()

        return Response({'messge':"registration completed"},status=status.HTTP_201_CREATED)


class RegisteredUserView(ListAPIView):
    Serializer_class = UsersSerializer