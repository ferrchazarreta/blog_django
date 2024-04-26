from django.urls import path, include
from products.views import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
)

urlpatterns = [
    path(route='', name='product_list', view=product_list),
    path(route='create/', name='product_create', view=product_create),
    path(route='<int:id>/', name='product_detail', view=product_detail),
    path(route='<int:id>/update/', name='product_update', view=product_update),
    path(route='<int:id>/delete', name='product_delete', view=product_delete),
]

