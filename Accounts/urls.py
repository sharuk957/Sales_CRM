from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('Registration',views.RegisterationView.as_view(),name='registration'),
    path('',views.LoginView.as_view(),name="login"),
    path('otplogin',views.OtpLoginView.as_view(),name="otplogin"),
    path('otpchecking',views.OtpCheckView.as_view(),name="otpchecking"),
    path('invitation',views.InvitationView.as_view(),name="invitation"),
    path('teamsignup',views.TeamSignUpView.as_view(),name="teamsignup"),
    path('viewregistration',views.RegisteredUserView.as_view(),name="viewregistration"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
