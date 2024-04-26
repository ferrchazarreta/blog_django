from products.models import Product, Category
from typing import (
    List,
    Optional,
)
class ProductRepository:
    def create(
        self, 
        nombre: str, 
        precio: float, 
        stock: int,
        categoria: Optional[Category] = None, 
        descripcion: Optional[str] = 'Sin Descripcion', 
        ) -> Product.objects:
        return Product.objects.create(
            name = nombre,
            description = descripcion,
            price = precio,
            category = categoria,
            stock = stock,
            )
    def get_all(self) -> List[Product]:
        return Product.objects.all()
    
    def get_by_id(
        self,
        id,
        ) -> Optional[Product]:
        return Product.objects.filter(id=id).first()
    
    def get_product_on_price_range(
        self,
        min_price = float,
        max_price = float,
    ) -> List[Product]:
        return Product.objects.filter(
            price__range = (min_price,max_price)
        )
    
    def delete_product(
        self,
        producto
        ):
        return producto.delete()