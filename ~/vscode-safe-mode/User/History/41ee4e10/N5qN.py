from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import studentEnrollment

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=150,widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User   
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('password do not match')
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField( max_length=150, label="UserName",required=True, widget=forms.TextInput)
    password = forms.CharField(label='password',required=True,widget=forms.PasswordInput)
        
 class EnrollmentForm(forms.Form):
    class Meta:
        model = studentEnrollment
        fields = ['senrollment_id ','sname','sid','level','semail','enroll_for', 'course_code']
