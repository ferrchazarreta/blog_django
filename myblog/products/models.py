from django.contrib import admin
from django.db import models
from django.utils.html import format_html
# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=200,
        )
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        null=True
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        )
        
    @admin.display(description='Rango de Precios')
    def get_price_range(self):
        if self.price > 1000000:
            return 'Alto'
        if 500000 < self.price < 1000000:
            return 'Medio' 
        else: 
            return 'Bajo'
    
    @admin.display(description='total')
    def get_total(self):
        return (self.price * self.stock)
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    