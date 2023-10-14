from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path('delete-product/<int:id>/', views.delete_product, name="delete_product"),
    path('update-product/<int:id>/', views.update_product, name="update_product"),
]