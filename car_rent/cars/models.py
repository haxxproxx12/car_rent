from django.db import models
from users.models import User
from datetime import date
from django.utils import timezone

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
    quantity = models.PositiveIntegerField(default=0)
    carClass = models.ForeignKey(CarClasses, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.model

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_days(self):
        rental_days = (self.end_date - self.start_date).days
        return rental_days

    def total_price(self):
        rental_days = (self.end_date - self.start_date).days
        return rental_days * self.car.price * self.quantity

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

class RentalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    rented_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"История аренды {self.user.username} - {self.car.brand} {self.car.model}"