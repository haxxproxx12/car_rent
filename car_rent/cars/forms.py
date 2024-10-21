from cars.models import Basket, Cars
from django import forms
from django.utils import timezone

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),  # Минимум - сегодня
            'end_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),  # Минимум - сегодня
        }
