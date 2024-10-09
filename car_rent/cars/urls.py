from django.urls import path
from cars.views import rent, cart_add, cart_delete, page_car

app_name = 'cars'

urlpatterns = [
    path('', rent, name='index'),
    path('cart-add/<int:car_id>', cart_add, name='cart_add'),
    path('cart-delete/<int:cart_id>', cart_delete, name='cart_delete'),
    path('car/<int:car_id>', page_car, name='page_car'),
]