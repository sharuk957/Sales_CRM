from django.contrib.auth.models import Permission
from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView,GenericAPIView
from .serializers import UsersSerializer,AccountSerializer,LoginSerializer
from .models import Users,Account
import jwt,datetime
from django.contrib.auth import authenticate


# Create your views here.

class RegisterationView(CreateAPIView):

    serializer_class = UsersSerializer

    def post(self, request, *args, **kwargs):
        role=Account.objects.get(role="Super Admin")
        update_request = request.data.copy()
        update_request.update({'role':role.pk})
        serializer = self.get_serializer(data=update_request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('success')

class RoleRegistrationView(CreateAPIView):

    serializer_class = AccountSerializer


class LoginView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self,request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email,password=password)
        print(user)
        if user is None:
            return Response({'message':'invalid Credential'},status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.serializer_class(user)
        print(serializer.data)
        return Response(serializer.data)