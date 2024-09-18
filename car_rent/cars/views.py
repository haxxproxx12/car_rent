from django.shortcuts import render
from operator import itemgetter


cars_services = {
        'cars': [
            {'name': 'KIA', 'discription': 'Экономичный автомобиль для повседневных поездок по городу и за его пределы.', 'class': 'Эконом', 'img': 'img/cars/car1/car1-1.jpg'},
            {'name': 'BMW', 'discription': 'Спортивный автомобиль для активных людей, которые ценят скорость и комфорт.', 'class': 'Спорт', 'img': 'img/cars/car2/car2-1.jpg'},
            {'name': 'Audi', 'discription': 'Премиум класс, удобный и стильный автомобиль для деловых встреч и мероприятий.', 'class': 'Премиум', 'img': 'img/cars/car3/car3-1.jpg'},
            {'name': 'Mercedes-Benz', 'discription': 'Люксовый автомобиль для тех, кто предпочитает высококлассное обслуживание.', 'class': 'Бизнес', 'img': 'img/cars/car4/car4-1.jpg'},
            {'name': 'Skoda', 'discription': 'Надежный автомобиль комфорт-класса для семейных поездок и дальних путешествий.', 'class': 'Комфорт', 'img': 'img/cars/car5/car5-1.jpg'},
            {'name': 'Volvo', 'discription': 'Безопасный и надежный автомобиль для тех, кто ценит качество и безопасность.', 'class': 'Комфорт', 'img': 'img/cars/car6/car6-1.jpg'},
        ],
        'services': [
            {'name': 'Фотосессия на фоне авто', 'discription': 'Организуем профессиональную фотосессию с вашими любимыми автомобилями. Отличный выбор для особых событий или для создания уникального контента в социальных сетях.'},
            {'name': 'Аренда авто на мероприятие', 'discription': 'Идеальное решение для свадьбы, корпоратива или любого другого важного события. Предоставим вам автомобиль, который подчеркнёт вашу важность на мероприятии.'},
            {'name': 'Трансфер в аэропорт', 'discription': 'Удобный и быстрый трансфер в любой аэропорт. Мы заберем вас вовремя и доставим в нужное место с комфортом.'},
            {'name': 'Аренда автомобиля с водителем', 'discription': 'Не хотите беспокоиться о вождении? Возьмите автомобиль вместе с опытным водителем, чтобы расслабиться и наслаждаться поездкой.'},
        ],
        'classes': [
            {'name': 'Кроссовер'},
            {'name': 'Премиум'},
            {'name': 'Эконом'},
            {'name': 'Комфорт'},
            {'name': 'Бизнес'},
            {'name': 'Спорт'},
        ]
}
# Create your views here.

def index(request):
    sort = cars_services
    sort['cars'].sort(key=itemgetter('name'))
    context = dict(sort)
    return render(request, 'cars/index.html', context)

def rent(request):
    sort = cars_services
    sort['cars'].sort(key=itemgetter('name'))
    sort['classes'].sort(key=itemgetter('name'))
    context = dict(sort)
    return render(request, 'cars/rent.html', context)

def about(request):
    
    return render(request, 'cars/about.html')