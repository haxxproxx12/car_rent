from django.db import models
from users.models import User
from datetime import date
from django.utils import timezone
from django.conf import settings

# Create your models here.

# Модель - это и есть таблица

class CarClasses(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class CarBrands(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return self.name

class Cars(models.Model):
    brand = models.ForeignKey(CarBrands, on_delete=models.PROTECT)
    model = models.CharField(max_length=64)
    year = models.IntegerField()
    image = models.ImageField(upload_to='car_img', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    carClass = models.ForeignKey(CarClasses, on_delete=models.PROTECT)
    is_rented = models.BooleanField(default=False)
    color = models.CharField(max_length=64, null=True, blank=True)
    drive = models.CharField(max_length=64, null=True, blank=True)
    transmission = models.CharField(max_length=64, null=True, blank=True)
    power = models.IntegerField(null=True, blank=True)
    acceleration = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    

    def __str__(self) -> str:
        return self.model

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_days(self):
        if self.start_date == self.end_date:
            return (self.end_date - self.start_date).days + 1
        return (self.end_date - self.start_date).days

    def total_price(self):
        return self.total_days() * self.car.price
    
    @property
    def total(self):
        return self.total_days() * int(self.car.price)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

class RentalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    rented_at = models.DateTimeField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)
    

    def __str__(self):
        return f"История аренды {self.user.username} - {self.car.brand} {self.car.model}"

class CarImage(models.Model):
    car = models.ForeignKey('Cars', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='car_img')

    def __str__(self):
        image_name = self.image.name.rsplit('/')
        return f'Изображение "{image_name[1]}" для {self.car.model}'
    
class PaymentInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, verbose_name="Номер карты")
    card_holder = models.CharField(max_length=100, verbose_name="Имя владельца")
    expiry_date = models.DateField(verbose_name="Срок действия")
    payment_system = models.CharField(
        max_length=50, 
        choices=[
            ('visa', 'Visa'),
            ('mastercard', 'MasterCard'),
            ('mir', 'MIR'),
            ('paypal', 'PayPal'),
            ('yandex', 'Yandex Money'),
            ('qiwi', 'QIWI')
        ],
        verbose_name="Платёжная система"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_system} - {self.card_number[-4:]}"