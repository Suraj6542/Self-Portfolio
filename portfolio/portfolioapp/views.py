from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def index(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Description=request.POST['Description']
        ContactMessage.objects.create(name=Name, email=Email, message=Description)
        messages.success(request,'Data has been submitted')

    return render(request,'index.html')
    