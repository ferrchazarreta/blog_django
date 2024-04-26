from django.shortcuts import render, redirect
from django.http import HttpResponse

from products.repositories.product_repository import ProductRepository

# Create your views here.

repo = ProductRepository()

def product_list(request):
    products = repo.get_all()
    return render(
        request,
        'product/list.html',
        dict(
            productos = products
        )
    )
    
def product_create(request):
    pass

def product_detail(request, id):
    producto = repo.get_by_id(id=id)
    return render(request, 'product/detail.html',{'producto':producto})

def product_delete(request, id):
    producto = repo.get_by_id(id)
    repo.delete_product(producto)
    return redirect('product_list')

def product_update(request):
    pass