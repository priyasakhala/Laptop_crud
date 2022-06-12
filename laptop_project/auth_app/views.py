from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from random import randint
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.


def RegisterView(request):
    form = UserCreationForm()
    template_name = 'app1/registerfile.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage_url')
    context = {'form': form}
    return render(request, template_name, context)

otp = randint(100000,999999)

def LoginView(request):
    template_name = 'app1/loginform.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('u')
        pw = request.POST.get('p')
        eml = request.POST.get('e')

        global new
        user = authenticate(username=un, password=pw)
        new = user
        if user is not None:
                subject = ' WELCOME TO ELITE INSTITUTE'
                message = f'Hi {user.username},{eml}, your otp is: {otp} THANK U!!'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ["piyasakhala2512@gmail.com"]
                send_mail(subject, message, email_from, recipient_list,fail_silently=True)  # send_mail(subject, message, from_email, to_list, fail_silently=Tre)
                return redirect('otp_url')
        context = {}
    return render(request, template_name, context)

def LogoutView(request):
    logout(request)
    return redirect("loginpage_url")

def OTPView(request):
    template_name = 'auth_app/otp.html'
    context = {}
    if request.method == 'POST':
        otp1 = int(request.POST.get('otp'))
        if otp == otp1:
            login(request,new)
            return redirect('showlap_url')
    return render(request,template_name,context)
