from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User   
        fields = ['Username','email','password']

    def clean_data(self):
        
    
