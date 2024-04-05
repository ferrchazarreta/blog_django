from django.contrib import admin
from products.models import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'description',
                    'price',
                    'category',
    )
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',
    )