from django.urls import path
from cars.views import rent, cart_delete, page_car, price_view, services_view, conditions_view

app_name = 'cars'

urlpatterns = [
    path('', rent, name='index'),
    # path('cart-add/<int:car_id>', cart_add, name='cart_add'),
    path('cart-delete/<int:cart_id>', cart_delete, name='cart_delete'),
    path('car/<int:car_id>', page_car, name='page_car'),
    path('price/', price_view, name='price'),
    path('services/', services_view, name='services'),
    path('conditions/', conditions_view, name='conditions'),
]