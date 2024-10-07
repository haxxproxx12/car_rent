from django.shortcuts import render
from cars.models import CarClasses, Cars, CarBrands
from cars.models import Basket, RentalHistory
from django.contrib.auth.decorators import login_required

cars_services = {
        'cars': Cars.objects.order_by('brand').all(),
        'classes': CarClasses.objects.order_by('name').all(),
        'brands': CarBrands.objects.order_by('name').all(),
        'services': [
            {'name': 'Фотосессия на фоне авто', 'discription': 'Организуем профессиональную фотосессию с вашими любимыми автомобилями. Отличный выбор для особых событий или для создания уникального контента в социальных сетях.'},
            {'name': 'Аренда авто на мероприятие', 'discription': 'Идеальное решение для свадьбы, корпоратива или любого другого важного события. Предоставим вам автомобиль, который подчеркнёт вашу важность на мероприятии.'},
            {'name': 'Трансфер в аэропорт', 'discription': 'Удобный и быстрый трансфер в любой аэропорт. Мы заберем вас вовремя и доставим в нужное место с комфортом.'},
            {'name': 'Аренда автомобиля с водителем', 'discription': 'Не хотите беспокоиться о вождении? Возьмите автомобиль вместе с опытным водителем, чтобы расслабиться и наслаждаться поездкой.'},
        ],
}
# Create your views here.

def index(request):
    context = cars_services
    return render(request, 'cars/index.html', context)

def rent(request):
    context = cars_services
    return render(request, 'cars/rent.html', context)

def about(request):
    
    return render(request, 'cars/about.html')

@login_required
def basket(request):
    # Получаем текущие товары в корзине пользователя
    basket_items = Basket.objects.filter(user=request.user)
    
    # Рассчитываем общую сумму аренды
    total_price = sum([item.total_price() for item in basket_items])

    if request.method == 'POST':
        # Обработка отправки корзины в историю аренды
        for item in basket_items:
            # Создаем запись в истории аренды
            RentalHistory.objects.create(
                user=request.user,
                car=item.car,
                start_date=item.start_date,
                end_date=item.end_date,
                total_price=item.total_price()
            )
        # Очищаем корзину после оформления
        basket_items.delete()
        return redirect('rental_history')  # Перенаправление на страницу истории аренды

    context = {
        'cart_items': basket_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)