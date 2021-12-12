from django.urls import path
from . import views


urlpatterns = [
    path('Registration',views.RegisterationView.as_view(),name='registration'),
    path('',views.LoginView.as_view(),name="login"),
    path('otplogin',views.OtpLoginView.as_view(),name="otplogin"),
    path('otpchecking',views.OtpCheckView.as_view(),name="otpchecking"),

]
