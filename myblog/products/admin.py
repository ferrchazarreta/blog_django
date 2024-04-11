from django.contrib import admin
from products.models import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('price','name','category__name',)
    list_editable = ('price', )
    list_display = ('name',
                    'description',
                    'price',
                    'category',
    )
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',
    )