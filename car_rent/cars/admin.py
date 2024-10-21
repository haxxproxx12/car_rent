from django.contrib import admin
from django.db.models import QuerySet
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
    list_display = ('brand', 'model', 'year', 'price', 'is_rented', 'carClass',)

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date',)

@admin.register(RentalHistory)
class RentalHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'total_price', 'rented_at', 'is_returned',)
    actions = ['set_return']

    @admin.action(description='Установить статус "is_returned"')
    def set_return(self, request, qs: QuerySet):
        qs.update(is_returned=True)

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'image',)

class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('car', 'start_date', 'end_date', 'total',)
    extra = 0
    readonly_fields = ('added_at', 'total',)
