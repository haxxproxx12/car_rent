from django.contrib import admin
from cars.models import CarClasses, Cars

# Register your models here.

admin.site.register(CarClasses)
admin.site.register(Cars)