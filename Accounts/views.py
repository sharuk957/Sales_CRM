from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView,GenericAPIView
from rest_framework.views import APIView
from .serializers import UsersSerializer,LoginSerializer
from .models import Users,Account
from django.contrib.auth import authenticate,login
from .twilio import send_sms,checking

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
            if Users.objects.filter(email=request.data['mobile_number']):
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
