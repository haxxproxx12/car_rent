from django.urls import path
from cars.views import rent

app_name = 'cars'

urlpatterns = [
    path('', rent, name='index'),

]