from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms
from cars.models import PaymentInfo

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

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'id': 'password2', 'placeholder': 'Подтвердите пароль'}),)

    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Введите email'}))

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image')

    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True,}))

    email = forms.CharField(widget=forms.TextInput(attrs={'readonly': True,}))

    first_name = forms.CharField(required=False, widget=forms.TextInput())

    last_name = forms.CharField(required=False, widget=forms.TextInput())

    image = forms.ImageField(widget=forms.FileInput(), required=False)


class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = PaymentInfo
        fields = ['card_number', 'card_holder', 'expiry_date', 'payment_system']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'card_number': forms.TextInput(attrs={'placeholder': 'Введите номер карты'}),
            'card_holder': forms.TextInput(attrs={'placeholder': 'Имя владельца'}),
            'payment_system': forms.Select(),
        }
