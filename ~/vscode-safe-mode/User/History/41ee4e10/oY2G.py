from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User   
        fields = ['Username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('password do not match')
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField( max_length=150, lable="UserName",required=True, widget=forms.TextInput(attr={'class': 'form-control', 'placeholder':'Enter your name'}))
    password = forms.chaField(lable='password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}))
        
    
