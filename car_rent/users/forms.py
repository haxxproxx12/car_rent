from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms
from django_password_eye.fields import PasswordEye

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Введите имя пользователя'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'id': 'password', 'placeholder': 'Введите пароль','autocomplete': 'off','data-toggle': 'password'}))

    class Meta:      
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    model = User
    fields = ('username', 'email', 'password', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Введите имя пользователя'}))

    password = PasswordEye(widget=forms.PasswordInput(attrs={'type': 'password', 'id': 'password', 'placeholder': 'Введите пароль','autocomplete': 'off','data-toggle': 'password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'id': 'password2', 'placeholder': 'Подтвердите пароль','autocomplete': 'off','data-toggle': 'password'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Введите email'}))
