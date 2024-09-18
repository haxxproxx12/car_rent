from django.db import models

# Create your models here.

# Модель - это и есть таблица

class CarClasses(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

class Cars(models.Model):
    brand = models.CharField(max_length=64, unique=True)
    model = models.CharField(max_length=64)
    year = models.IntegerField()
    image = models.ImageField(upload_to='', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    carClass = models.ForeignKey(CarClasses, on_delete=models.PROTECT)
