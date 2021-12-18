from .models import Account,Users
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class AccountSerializer(ModelSerializer):

    class Meta:

        model = Account
        fields = '__all__'


class UsersSerializer(ModelSerializer):
    
    date_joined = serializers.DateField(read_only=True)
    last_login = serializers.DateField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:

        model = Users
        fields = '__all__'

    def create(self, validated_data):
        user = Users.objects.create_superuser(
            email = validated_data['email'],
            name = validated_data['name'],
            mobile_number = validated_data['mobile_number'],
            role = validated_data['role'],
            password = validated_data['password']
        )
        return user
       
