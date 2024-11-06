from cars.models import Basket, Cars, PaymentInfo
from django import forms
from django.utils import timezone


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date(), 'id': 'start_date'}),  # Минимум - сегодня
            'end_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date(), 'id': 'end_date'}),  # Минимум - сегодня
        }
    
    def clean_date(self, start_date, end_date):        
        if end_date < start_date:
            return False
        return True

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    phone_code = forms.ChoiceField(label='Код страны', choices=[('+7', '+7'), ('+1', '+1'), ('+44', '+44'), ('+49', '+49')], initial='+7', widget=forms.Select(attrs={'class': 'form-control phone-code'}))
    phone_number = forms.CharField(label='Номер телефона', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control phone-number', 'placeholder': '+7 999 999 99 99'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)

