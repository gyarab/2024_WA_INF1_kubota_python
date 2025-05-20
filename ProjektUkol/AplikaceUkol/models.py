from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length = 255) # Název výrobce
    established = models.PositiveIntegerField() # Počáteční rok výroby
    countryOfOrigin = models.CharField(max_length = 255) # Země původu
    defunct = models.BooleanField() # Jestli výrobce stále existuje

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 255, unique=True) # Název kategorie

    def __str__(self):
        return self.name
    
class CarSpecifications(models.Model):
    name = models.CharField(max_length = 255) # Název auta
    engine = models.CharField(max_length = 255) # Název motoru auta
    fuel = models.CharField(max_length = 255) # Palivo, které motor používá
    displacement = models.FloatField() # Objem motoru v litrech
    power = models.PositiveIntegerField()  # Výkon v kW (koně nebudou)
    kilometrageCity = models.FloatField() # Spotřeba ve městě na 100 km, odmítám imperiální jednotky
    kilometrageRoad = models.FloatField() # Spotřeba na silnicích na 100 km
    weight = models.PositiveIntegerField()  # Hmotnost v kg
    top_speed = models.PositiveIntegerField()  # Maximální rychlost v km/h
    zero_to_hundred = models.FloatField()  # Zrychlení 0-100 km/h v sekundách
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    car_review = models.ForeignKey(CarSpecifications, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.car_review.name}"