from django.shortcuts import render, redirect

from product.repositories.category import CategoryRepository

repo = CategoryRepository()

def category_list(request):
    categorias = repo.get_all()
    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )

def category_list(request):
    categorias = repo.get_all()
    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )

def category_delete(request, id):
    categoria = repo.get_by_id(id=id)
    repo.delete(categoria=categoria)
    return redirect('category_list')

def category_update(request, id):
    category = repo.get_by_id(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        repo.update(
            category,
            nombre=name,
        )
        return redirect('category_list')

    return render(
        request,
        'categories/update.html',
        dict(
            category=category
        )
    )

def category_create(request):
    categorias = repo.get_all()
    if request.method == "POST":
        name = request.POST.get('name')
        repo.create(
            nombre=name,
        )
        return redirect('category_list')
    return render (
        request,
        'categories/create.html',
        dict(
            categories=categorias
        )
    )

def index_view(request):
    return render(
        request,
        'index/index.html'
    )