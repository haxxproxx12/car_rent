from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from cars.models import CarClasses, Cars, CarBrands, Basket, RentalHistory
from cars.forms import BasketForm, ContactForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages


# Create your views here.

services = [
            {'name': 'Фотосессия на фоне авто', 'description': 'Организуем профессиональную фотосессию с вашими любимыми автомобилями. Отличный выбор для особых событий или для создания уникального контента в социальных сетях.'},
            {'name': 'Аренда авто на мероприятие', 'description': 'Идеальное решение для свадьбы, корпоратива или любого другого важного события. Предоставим вам автомобиль, который подчеркнёт вашу важность на мероприятии.'},
            {'name': 'Трансфер в аэропорт', 'description': 'Удобный и быстрый трансфер в любой аэропорт. Мы заберем вас вовремя и доставим в нужное место с комфортом.'},
            {'name': 'Аренда автомобиля с водителем', 'description': 'Не хотите беспокоиться о вождении? Возьмите автомобиль вместе с опытным водителем, чтобы расслабиться и наслаждаться поездкой.'},
        ]

def index(request):
    context = {
        'cars': Cars.objects.order_by('brand').all(),
        'classes': CarClasses.objects.order_by('name').all(),
        'brands': CarBrands.objects.order_by('name').all(),
        'title': 'АрендаRzn',
        'services': services,
}
    return render(request, 'cars/index.html', context)

def rent(request):
    car_classes = CarClasses.objects.all()
    car_brands = CarBrands.objects.all()
    selected_class = request.GET.get('class')
    selected_brand = request.GET.get('brand')

    cars = Cars.objects.all().order_by('brand__name')

    print(cars)
    
    if selected_class and selected_class != 'all':
        cars = cars.filter(carClass__name=selected_class)

    if selected_brand and selected_brand != 'all':
        cars = cars.filter(brand__name=selected_brand)

    context = {
    'car_classes': car_classes,
    'car_brands': car_brands,
    'cars': cars,
    'selected_class': selected_class,
    'selected_brand': selected_brand,
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
            if item.start_date == item.end_date:
                end_date = item.end_date + datetime.timedelta(days=1)
            else:
                end_date = item.end_date
            RentalHistory.objects.create(
                user=request.user,
                car=item.car,
                start_date=item.start_date,
                end_date=end_date,
                total_price=item.total_price(),
            )
        cart_items.delete()
        return redirect('/users/rental_history')

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'title': 'Корзина',
    }
    return render(request, 'cars/cart.html', context)



def cart_delete(request, cart_id):
    cart = Basket.objects.get(id=cart_id)
    car = cart.car
    car.is_rented = False
    car.save()
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# @login_required
def page_car(request, car_id):
    car = Cars.objects.get(id=car_id)
    images = car.images.all()
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    if request.method == 'POST':
        form = BasketForm(data=request.POST)
        if form.clean_date(start_date, end_date):
            if form.is_valid():
                if not request.user.is_authenticated:
                    request.session['car_form_data'] = request.POST
                    request.session['car_id'] = car_id
                    return redirect(f'/users/login?next={request.path}')
            if car.is_rented == True:
                messages.error(request, 'Автомобиль уже забронирован.')
            else: 
                basket_item = form.save(commit=False)
                basket_item.user = request.user
                basket_item.car = car
                basket_item.added_at = timezone.now()
                basket_item.save()
                
                car.is_rented = True
                car.save()
                return redirect('cart')
        else:
            form.add_error('end_date', 'Конечная дата не может быть меньше')
    else:
        if 'car_form_data' in request.session and 'car_id' in request.session and request.session['car_id'] == car_id:
            form = BasketForm(request.session['car_form_data'])
            del request.session['car_form_data']
        else:
            form = BasketForm()

    context = {
        'car': car,
        'form': form,
        'car_images': images,
    }
    return render(request, 'cars/car.html', context)

@login_required
def return_car(request, rental_id):
    rental = RentalHistory.objects.get(user=request.user, id=rental_id)
    if rental.is_returned == True:
        return redirect('/users/rental_history')
    
    car = Cars.objects.get(id=rental.car.id)
    print(car.is_rented)
    if car.is_rented == False:
        messages.error(request, 'Авто не забронировано')
    else:
        car.is_rented = False
        car.save()
        rental.is_returned = True
        rental.save()

    return redirect('/users/rental_history')

def price_view(request):
    cars = Cars.objects.all()
    context = {
        'title': 'Цены на автомобили',
        'cars': cars,
    }
    return render(request, 'cars/price.html', context)

def services_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        errors = form.errors
        if form.is_valid():
            messages.success(request, 'Спасибо за обращение! Мы свяжемся с вами в ближайшее время.')
            return redirect('cars:services')
        else:
            for error in errors:
                    messages.error(request, form.errors[error])
    else:
        form = ContactForm()

    context = {
        'title': 'Наши услуги',
        'services': services,
        'form': form,
    }
    return render(request, 'cars/services.html', context)

def conditions_view(request):
    context = {
        'title': 'Условия уренды',
    }
    return render(request, 'cars/conditions.html', context)

