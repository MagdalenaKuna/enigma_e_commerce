from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('products/new_product/', ProductCreate.as_view()),
    path('products/update/<int:pk>/', ProductUpdate.as_view()),
    path('products/delete/<int:pk>/', ProductDelete.as_view()),
]
