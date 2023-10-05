from django.urls import path
from .views import OrderCreate, OrderList

urlpatterns = [
    path('order/', OrderCreate.as_view(), name='order'),
    path('orders/', OrderList.as_view(), name='order_list'),
]
