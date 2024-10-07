from django.contrib import admin
from cars.models import CarClasses, Cars, CarBrands, Basket

# Register your models here.

admin.site.register(CarClasses)
admin.site.register(Cars)
admin.site.register(CarBrands)
admin.site.register(Basket)