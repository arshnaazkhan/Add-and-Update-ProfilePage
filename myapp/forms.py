from django.core import validators
from django import forms
from .models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name','email','contact_no','password']
        widgets = {
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True ,attrs={'class':'form-control'})
        }