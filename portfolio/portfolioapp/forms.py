from django import forms
from .models import ContactMessage
 
 
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"