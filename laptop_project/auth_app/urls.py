from django.urls import path
from . import views

urlpatterns = [

    path('reg/',views.RegisterView, name='register_url'),
    path('lin/',views.LoginView, name='loginpage_url'),
    path('lout/',views.LogoutView, name='logout_url'),
    path('otp/',views.OTPView, name='otp_url')
]