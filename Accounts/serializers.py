from django.db import models
from rest_framework.validators import UniqueValidator
from .models import Account,Users
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class AccountSerializer(ModelSerializer):

    class Meta:

        model = Account
        fields = '__all__'


class UsersSerializer(ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Users.objects.all())]
            )
    mobile_number = serializers.IntegerField(
            required=True,
            validators=[UniqueValidator(queryset=Users.objects.all())]
            )
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
        if validated_data['role'].role == 'Super Admin':
            user = Users.objects.create_superuser(
                email = validated_data['email'],
                name = validated_data['name'],
                mobile_number = validated_data['mobile_number'],
                role = validated_data['role'],
                password = validated_data['password']
            )
            return user
        elif validated_data['role'].role == 'Admin':
            user = Users.objects.create(
                email = validated_data['email'],
                name = validated_data['name'],
                mobile_number = validated_data['mobile_number'],
                role = validated_data['role'],
                password = validated_data['password']
            )
            user.is_admin = True
            user.is_staff = True
            user.save()
            return user
        else:
            user = Users.objects.create(
                email = validated_data['email'],
                name = validated_data['name'],
                mobile_number = validated_data['mobile_number'],
                company_name = validated_data['company_name'],
                role = validated_data['role'],
                password = validated_data['password']
            )
            return user

class LoginSerializer(ModelSerializer):

    class Meta:

        model = Users
        fields = ['token']

        read_only_fields = ['token']


