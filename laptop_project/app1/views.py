from django.shortcuts import render,redirect
import email
from multiprocessing import context
from re import template
from . models import Laptop
from .forms import LaptopForm
from django.contrib.auth.decorators import login_required
from email import message


# Create your views here.
@login_required(login_url='loginpage_url')
def LaptopView(request):
    form = LaptopForm()
    #print(form)
    template_name = 'app1/lapform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlap_url')
    return render(request, template_name, context)

@login_required(login_url='loginpage_url')
def ShowLaptopView(request):
    data = Laptop.objects.all()
    template_name = 'app1/showlap.html'
    context = {'obj': data}
    return render(request, template_name, context)

def UpdateLaptopView(request,id):
    obj = Laptop.objects.get(id=id)
    form = LaptopForm(instance=obj)
    template_name = 'app1/lapform.html'
    context = {'form':form}
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showlap_url')
    return render(request, template_name, context)

def DeleteLaptopView(request,id):
    obj = Laptop.objects.get(id = id)
    template_name = 'app1/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return  redirect('showlap_url')
    return  render(request, template_name, context)


