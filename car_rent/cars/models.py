from django.db import models

# Create your models here.

# Модель - это и есть таблица

class CarClasses(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

class CarBrands(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Cars(models.Model):
    brand = models.ForeignKey(CarBrands, on_delete=models.PROTECT)
    model = models.CharField(max_length=64)
    year = models.IntegerField()
    image = models.ImageField(upload_to='', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    carClass = models.ForeignKey(CarClasses, on_delete=models.PROTECT)
