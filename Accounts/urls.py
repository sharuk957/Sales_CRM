from django.urls import path
from . import views

urlpatterns = [
    path('Registration',views.RegisterationView.as_view()),
    path('',views.RoleRegistrationView.as_view())
]