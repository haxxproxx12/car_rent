from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from cars.models import CarClasses, Cars, CarBrands
from cars.models import Basket, RentalHistory
from cars.forms import RentDate
from django.contrib.auth.decorators import login_required
from datetime import date


# Create your views here.

def index(request):
    context = {
        'cars': Cars.objects.order_by('brand').all(),
        'classes': CarClasses.objects.order_by('name').all(),
        'brands': CarBrands.objects.order_by('name').all(),
        'title': 'АрендаRzn',
        'services': [
            {'name': 'Фотосессия на фоне авто', 'discription': 'Организуем профессиональную фотосессию с вашими любимыми автомобилями. Отличный выбор для особых событий или для создания уникального контента в социальных сетях.'},
            {'name': 'Аренда авто на мероприятие', 'discription': 'Идеальное решение для свадьбы, корпоратива или любого другого важного события. Предоставим вам автомобиль, который подчеркнёт вашу важность на мероприятии.'},
            {'name': 'Трансфер в аэропорт', 'discription': 'Удобный и быстрый трансфер в любой аэропорт. Мы заберем вас вовремя и доставим в нужное место с комфортом.'},
            {'name': 'Аренда автомобиля с водителем', 'discription': 'Не хотите беспокоиться о вождении? Возьмите автомобиль вместе с опытным водителем, чтобы расслабиться и наслаждаться поездкой.'},
        ],
}
    return render(request, 'cars/index.html', context)

def rent(request):
    context = {
        'cars': Cars.objects.order_by('brand').all(),
        'classes': CarClasses.objects.order_by('name').all(),
        'brands': CarBrands.objects.order_by('name').all(),
        'title': 'Автопарк',
}
    return render(request, 'cars/rent.html', context)

def about(request):
    context = {
        'title': 'О нас'
    }
    return render(request, 'cars/about.html', context)

@login_required
def cart(request):
    cart_items = Basket.objects.filter(user=request.user)
    total_price = sum([item.total_price() for item in cart_items])

    if request.method == 'POST':
        for item in cart_items:
            RentalHistory.objects.create(
                user=request.user,
                car=item.car,
                start_date=item.start_date,
                end_date=item.end_date,
                total_price=item.total_price(),
                quantity=item.quantity
            )
        cart_items.delete()
        return redirect('users/rental_history')

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'title': 'Корзина',
    }
    return render(request, 'cars/cart.html', context)

@login_required
def cart_add(request, car_id):
    car = Cars.objects.get(id=car_id)
    cart_items = Basket.objects.filter(user=request.user, car=car)
    if not cart_items.exists():
        Basket.objects.create(user=request.user, car=car, quantity=1, start_date=date.today, end_date=date.today)
        return HttpResponseRedirect('index')
    else:
        cart = cart_items.first()
        cart.quantity += 1
        cart.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def cart_delete(request, cart_id):
    cart = Basket.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def page_car(request, car_id):
    if request.method == 'POST':
        form = RentDate(data=request.POST)
        if form.is_valid():
            cart_add(request, car_id)
            return HttpResponseRedirect(reverse('users:rental_history'))
    else:
        # form = UserProfileForm(instance=request.user)
        pass
    car = Cars.objects.get(id=car_id)
    context = {
        'car': car,
        'title': 'Корзина',
    }
    return render(request, 'cars/car.html', context)
