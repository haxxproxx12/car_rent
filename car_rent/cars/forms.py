from cars.models import Basket, Cars
from django import forms
from django.utils import timezone

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['start_date', 'end_date', 'quantity']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),  # Минимум - сегодня
            'end_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),  # Минимум - сегодня
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        self.max_quantity = kwargs.pop('max_quantity')  # Получаем максимальное количество автомобилей
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['max'] = self.max_quantity  # Устанавливаем максимальное количество

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity > self.max_quantity:
            raise forms.ValidationError(f'Вы можете арендовать не более {self.max_quantity} автомобилей.')
        return quantity