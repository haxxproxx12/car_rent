from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Введите имя пользователя'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'id': 'password', 'placeholder': 'Введите пароль','autocomplete': 'off','data-toggle': 'password'}))

    class Meta:      
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Введите имя пользователя'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'id': 'password', 'placeholder': 'Введите пароль'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'id': 'password2', 'placeholder': 'Подтвердите пароль'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Введите email'}))
