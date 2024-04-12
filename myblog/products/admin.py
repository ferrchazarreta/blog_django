from django.contrib import admin
from products.models import Product, Category
from django.utils.html import format_html

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('price','name','category__name',)
    list_editable = ('price', )
    empty_value_display = 'No hay datos'
    readonly_fields = ('name')
    list_display = ('name',
                    'description',
                    'price',
                    'category',
                    'get_price_range',
                    'stock',
                    'get_total',
                    'get_stock',
    )

    def get_total(self):
        return (self.price * self.stock)
    
    def get_stock (self,obj):
        POCO = '#FF0000'
        MUCHO = '#008000'
        ESCASO = '#FFD300'
        codigo = ESCASO
        if obj.stock > 10:
            codigo = POCO
        if obj.stock > 50:
            codigo = MUCHO
        return format_html(
            '<span style="color:{}">{}</span>',
            codigo, obj.stock,
        )    
    
    fieldsets = [
        (
            'Informacion del producto',
            {
                'fields':['name','price'],
            }
        ),
        (
            'Mas informacion del producto',
            {
                'classes':['collapse'],
                'fields':['description','stock']
            }
        )
    ]
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',
    )