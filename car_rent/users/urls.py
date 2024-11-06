from django.urls import path
from users.views import login, register, user_profile, user_logout, rental_history, payment_view, delete_payment_method
from cars.views import return_car

app_name = 'users'

urlpatterns = [
    path('login', login, name='login'),
    path('registration', register, name='register'),
    path('profile', user_profile, name='profile'),
    path('logout', user_logout, name='logout'),
    path('rental_history', rental_history, name='rental_history'),
    path('return/<int:rental_id>/', return_car, name='return_car'),
    path('payment/', payment_view, name='payment'),
    path('payment/delete/<int:payment_id>/', delete_payment_method, name='delete_payment'),
]