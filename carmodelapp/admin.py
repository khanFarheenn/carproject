from django.contrib import admin
from .models import Car, Owner
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'make', 'model', 'year', 'price', 'color', 'owner']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
