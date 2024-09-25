from django.contrib.auth.forms import AuthenticationForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            "user_name": "*Username",
            "password": "*Password"
        }    
        widgets = {
            "user_name":  forms.TextInput(attrs={'placeholder':'ex:test','autocomplete': 'off'}), 
            "password": forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
        }