from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import CarSpecifications, Category, Manufacturer

def index(request):
    cars = CarSpecifications.objects.all()
    categories = Category.objects.all()
    manufacturers = Manufacturer.objects.all()
    return render(request, 'AplikaceUkol/index.html', {'cars': cars, 'categories': categories, 'manufacturers': manufacturers})

def car_detail(request, pk):
    car = get_object_or_404(CarSpecifications, pk=pk)
    categories = car.categories.all()
    manufacturer = car.manufacturer
    return render(request, 'AplikaceUkol/car_detail.html', {'car': car, 'categories': categories, 'manufacturer': manufacturer})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)  # Získání kategorie podle ID
    cars = CarSpecifications.objects.filter(categories=category)  # Filtrování aut podle kategorie
    return render(request, 'AplikaceUkol/category_detail.html', {'category': category, 'cars': cars})

def manufacturer_detail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    cars = CarSpecifications.objects.filter(manufacturer=manufacturer)
    return render(request, 'AplikaceUkol/manufacturer_detail.html', {'manufacturer': manufacturer, 'cars': cars})