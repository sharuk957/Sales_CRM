from django.conf import settings
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import  CustomerSerializer, ProductSerializer
from .models import  Person, Product
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet



class ProductView(ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer


class CustomerView(CreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomerSerializer

    def post(self,request):
        print('hi')
        owner = request.user.name
        owner_email = request.user.email
        name = request.data.get('name')
        mobile_num = request.data.get('mobile_num')
        email = request.data.get('email')
        if Person.objects.filter(email__contains=[email]):
            return Response({'message':'Email already Exist'},status=status.HTTP_208_ALREADY_REPORTED)
        if Person.objects.filter(mobile_num__contains=[mobile_num]):
            return Response({'message':'Mobile number already Exist'},status=status.HTTP_208_ALREADY_REPORTED)

        Person.objects.create(name=name,owner=owner,owner_email=owner_email,email=[email],mobile_num=[mobile_num])
        return Response({'message':"success"},status=status.HTTP_201_CREATED)



class CustomerManagmentView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = CustomerSerializer

class CustomerListView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = CustomerSerializer

