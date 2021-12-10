from django.contrib.auth.models import Permission
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from rest_framework import serializers
import rest_framework
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView
from .serializers import UsersSerializer
from .models import Users,Account
# Create your views here.

class RegisterationView(CreateAPIView):
    serializer_class = UsersSerializer
    def post(self, request, *args, **kwargs):
        role=Account.objects.get(role="Super Admin")
        update_request = request.data.copy()
        update_request.update({'role':role.pk})
        serializer = self.get_serializer(data=update_request)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response('success')
