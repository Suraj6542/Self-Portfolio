from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages
import pandas as pd

def index(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Description=request.POST['Description']
        ContactMessage.objects.create(name=Name, email=Email, message=Description)
        messages.success(request,'Data has been submitted')
        export_data_to_excel()

    return render(request,'index.html')

def export_data_to_excel():
    queryset = ContactMessage.objects.all()
    df = pd.DataFrame(list(queryset.values()))
    excel_file_path = 'C:/Users/hp/Downloads/Portfolio_data.xlsx'
    df.to_excel(excel_file_path, index=False)

    