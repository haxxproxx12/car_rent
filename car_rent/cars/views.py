from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from cars.models import CarClasses, Cars, CarBrands
from cars.models import Basket, RentalHistory
from cars.forms import BasketForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import datetime


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
    car_classes = CarClasses.objects.all()
    car_brands = CarBrands.objects.all()
    selected_class = request.GET.get('class')
    selected_brand = request.GET.get('brand')

    cars = Cars.objects.all()
    
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
                quantity=item.quantity
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
    car.quantity += cart.quantity
    car.save()
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# @login_required
def page_car(request, car_id):
    car = Cars.objects.get(id=car_id)
    images = car.images.all()
    print('это картинки - ', images)
    if request.method == 'POST':
        form = BasketForm(data=request.POST, max_quantity=car.quantity)
        if form.is_valid():
            if not request.user.is_authenticated:
                request.session['car_form_data'] = request.POST
                request.session['car_id'] = car_id
                return redirect(f'/users/login?next={request.path}')


            basket_item = form.save(commit=False)
            basket_item.user = request.user
            basket_item.car = car
            basket_item.added_at = timezone.now()
            if basket_item.quantity > car.quantity:
                form.add_error('quantity', 'Недостаточно автомобилей для аренды.')
            else:
                car.quantity -= basket_item.quantity
                car.save()

                basket_item.save()
                return redirect('cart')
    else:
        if 'car_form_data' in request.session and 'car_id' in request.session and request.session['car_id'] == car_id:
            form = BasketForm(request.session['car_form_data'], max_quantity=car.quantity)
            del request.session['car_form_data']  # Удаляем данные формы после использования
        else:
            form = BasketForm(max_quantity=car.quantity)

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

    car = rental.car
    car.quantity += rental.quantity
    car.save()

    rental.is_returned = True
    rental.save()

    return redirect('/users/rental_history')

