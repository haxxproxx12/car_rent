from cars.models import Basket, Cars
from django import forms

class RentDate():
    class META:
        model = Basket
        fields = {'start_date', 'end_date'}
    
    start_date = forms.DateField(widget=forms.DateInput())
    end_date = forms.DateField(widget=forms.DateInput())