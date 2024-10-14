from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth import logout
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User
from cars.models import Basket, RentalHistory
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {'form': form,
            'title': 'Вход',}
    return render(request, 'users/login.html', context)


    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message='Регистрация прошла успешно')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form,
               'title': 'Регистрация',}
    return render(request, 'users/register.html', context)

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form,
               'title': 'Профиль',}
    return render(request, 'users/profile.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def rental_history(request):
    context = {'history_items': RentalHistory.objects.filter(user=request.user),
               'title': 'История аренды',}
    return render(request, 'users/rental_history.html', context)