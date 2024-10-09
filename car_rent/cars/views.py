from django.shortcuts import render, redirect
from cars.models import CarClasses, Cars, CarBrands
from cars.models import Basket, RentalHistory
from django.contrib.auth.decorators import login_required


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
    # Получаем текущие товары в корзине пользователя
    cart_items = Basket.objects.filter(user=request.user)
    
    # Рассчитываем общую сумму аренды
    total_price = sum([item.total_price() for item in cart_items])

    if request.method == 'POST':
        # Обработка отправки корзины в историю аренды
        for item in cart_items:
            # Создаем запись в истории аренды
            RentalHistory.objects.create(
                user=request.user,
                car=item.car,
                start_date=item.start_date,
                end_date=item.end_date,
                total_price=item.total_price()
            )
        # Очищаем корзину после оформления
        cart_items.delete()
        return redirect('users/rental_history')  # Перенаправление на страницу истории аренды

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'title': 'Корзина',
    }
    return render(request, 'cars/cart.html', context)