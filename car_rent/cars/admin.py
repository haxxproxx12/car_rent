from django.contrib import admin
from cars.models import CarClasses, Cars, CarBrands, Basket, RentalHistory, CarImage

# Register your models here.

admin.site.register(CarClasses)
admin.site.register(Cars)
admin.site.register(CarBrands)
admin.site.register(Basket)
admin.site.register(RentalHistory)
admin.site.register(CarImage)