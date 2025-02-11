from django.contrib import admin
from .models import CarSpecifications, Category, Manufacturer

admin.site.register(CarSpecifications)
admin.site.register(Category)
admin.site.register(Manufacturer)