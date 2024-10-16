from django.contrib import admin
from users.models import User
from cars.admin import BasketAdminInline


# Register your models here.

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
    # list_display = ('car', 'quantity', 'start_date', 'end_date', 'total_price',)
