from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'RENT',
        'header': 'HELLO WORLD',
        'cars': [
            {'name': 'Car Model 1', 'discription': 'Описание автомобиля: класс, марка, особенности.', 'img': 'img/cars/car1/car1-1.jpg'},
            {'name': 'Car Model 2', 'discription': 'Описание автомобиля: класс, марка, особенности.', 'img': 'img/cars/car2/car2-1.jpg'},
            {'name': 'Car Model 3', 'discription': 'Описание автомобиля: класс, марка, особенности.', 'img': 'img/cars/car3/car3-1.jpg'},
            {'name': 'Car Model 4', 'discription': 'Описание автомобиля: класс, марка, особенности.', 'img': 'img/cars/car4/car4-1.jpg'},
            {'name': 'Car Model 5', 'discription': 'Описание автомобиля: класс, марка, особенности.', 'img': 'img/cars/car5/car5-1.jpg'},
            {'name': 'Car Model 6', 'discription': 'Описание автомобиля: класс, марка, особенности.', 'img': 'img/cars/car6/car6-1.jpg'},
        ],
        'services': [
            {'name': 'Фотосессия на фоне авто', 'discription': 'Организуем профессиональную фотосессию с вашими любимыми автомобилями. Отличный выбор для особых событий или для создания уникального контента в социальных сетях.'},
            {'name': 'Аренда авто на мероприятие', 'discription': 'Идеальное решение для свадьбы, корпоратива или любого другого важного события. Предоставим вам автомобиль, который подчеркнёт вашу важность на мероприятии.'},
            {'name': 'Трансфер в аэропорт', 'discription': 'Удобный и быстрый трансфер в любой аэропорт. Мы заберем вас вовремя и доставим в нужное место с комфортом.'},
            {'name': 'Аренда автомобиля с водителем', 'discription': 'Не хотите беспокоиться о вождении? Возьмите автомобиль вместе с опытным водителем, чтобы расслабиться и наслаждаться поездкой.'},
        ],

    }
    return render(request, 'cars/index.html', context)

def rent(request):

    return render(request, 'cars/rent.html')

def test_context(request):
    context = {
        'title': 'RENT',
        'header': 'HELLO WORLD',
        'cars': [
            {'name': 'Car Model 1', 'discription': 'Описание автомобиля: класс, марка, особенности.'},
            {'name': 'Car Model 2', 'discription': 'Описание автомобиля: класс, марка, особенности.'},
            {'name': 'Car Model 3', 'discription': 'Описание автомобиля: класс, марка, особенности.'},
            {'name': 'Car Model 4', 'discription': 'Описание автомобиля: класс, марка, особенности.'},
            {'name': 'Car Model 5', 'discription': 'Описание автомобиля: класс, марка, особенности.'},
            {'name': 'Car Model 6', 'discription': 'Описание автомобиля: класс, марка, особенности.'},
        ]
    }
    return render(request, 'cars/test_context.html', context)