from django.shortcuts import render, redirect

from product.repositories.supplier import SupplierRepository

repo = SupplierRepository()

def supplier_list(request):
    proveedores = repo.get_all()
    return render(
        request,
        'categories/list.html',
        dict(
            suppliers=proveedores
        )
    )

def supplier_list(request):
    proveedores = repo.get_all()
    return render(
        request,
        'suppliers/list.html',
        dict(
            suppliers=proveedores
        )
    )

def supplier_delete(request, id):
    proveedor = repo.get_by_id(id=id)
    repo.delete(proveedor=proveedor)
    return redirect('supplier_list')

def supplier_update(request, id):
    supplier = repo.get_by_id(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        repo.update(
            supplier,
            nombre=name,
        )
        return redirect('supplier_list')

    return render(
        request,
        'suppliers/update.html',
        dict(
            supplier=supplier
        )
    )

def supplier_create(request):
    proveedores = repo.get_all()
    if request.method == "POST":
        name = request.POST.get('name')
        repo.create(
            nombre=name,
        )
        return redirect('supplier_list')
    return render (
        request,
        'suppliers/create.html',
        dict(
            suppliers=proveedores
        )
    )

def supplier_detail(request, id):
    supplier = repo.get_by_id(id=id)
    return render(
        request,
        'suppliers/detail.html',
        {"supplier":supplier}
    )
    
def index_view(request):
    return render(
        request,
        'index/index.html'
    )