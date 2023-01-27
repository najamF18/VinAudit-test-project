from django.contrib import admin
from .models import Car

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ("vin", "model", "make", "listing_price")


admin.site.register(Car, CarAdmin)
