from typing import List, Optional
from product.models import Supplier

class SupplierRepository:
    def get_all(self)-> List[Supplier]:
        return Supplier.objects.all()
    
    def filter_by_id(self, id: int) -> Optional[Supplier]:
        return Supplier.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Supplier]:
        try:
            supplier = Supplier.objects.get(id=id)
        except:
            supplier = None
        return supplier
    
    def create(
        self,
        nombre: str,
    ):
        return Supplier.objects.create(
            name=nombre,
        )
    
    def delete(self, proveedor: Supplier):
        return proveedor.delete()
    
    def update(
        self, 
        proveedor: Supplier,
        nombre: str,
        direccion: str,
        telefono: int,
        
    ) -> Supplier:
        proveedor.name = nombre
        proveedor.address = direccion
        proveedor.phone = telefono
        proveedor.save()
