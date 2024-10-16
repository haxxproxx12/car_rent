from django.contrib import admin
from cars.models import CarClasses, Cars, CarBrands, Basket, RentalHistory, CarImage

# Register your models here.



@admin.register(CarClasses)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarBrands)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'quantity', 'carClass',)

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'quantity',)

@admin.register(RentalHistory)
class RentalHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'total_price', 'rented_at', 'quantity', 'is_returned',)

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'image',)

class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('car', 'quantity', 'start_date', 'end_date', 'total',)
    extra = 0
    # list_display = ('car', 'quantity', 'start_date', 'end_date', 'total_price',)
    readonly_fields = ('added_at', 'total',)
