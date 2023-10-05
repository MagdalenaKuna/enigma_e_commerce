from django.urls import path
from .views import ProductStatistics


urlpatterns = [
    path('product_statistics/', ProductStatistics.as_view(), name='product_statistics'),
]