from typing import List, Optional
from product.models import Category

class CategoryRepository:
    def get_all(self)-> List[Category]:
        return Category.objects.all()
    
    def filter_by_id(self, id: int) -> Optional[Category]:
        return Category.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Category]:
        try:
            category = Category.objects.get(id=id)
        except:
            category = None
        return category
    
    def delete(self, categoria: Category):
        return categoria.delete()
    
    def update(
        self, 
        categoria: Category,
        nombre: str,
    ) -> Category:
        categoria.name = nombre
        categoria.save()

    def create(
        self,
        nombre: str,
    ) -> Category:
        category = Category.objects.filter(name=nombre)
        if category:
            return "Ya existe esa categoria"
        return Category.objects.create(
            name=nombre,
        )
    
