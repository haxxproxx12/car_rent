from django.urls import path
from users.views import login, register, user_profile, user_logout, rental_history

app_name = 'users'

urlpatterns = [
    path('login', login, name='login'),
    path('registration', register, name='register'),
    path('profile', user_profile, name='profile'),
    path('logout', user_logout, name='logout'),
    path('rental_history', rental_history, name='rental_history'),
]