from cars.models import Basket, Cars
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
    
    def clean_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        
        if end_date < start_date:
            return False
        return True
