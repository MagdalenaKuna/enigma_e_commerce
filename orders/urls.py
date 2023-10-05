from django.urls import path
from .views import OrderCreate

urlpatterns = [
    path('order/', OrderCreate.as_view(), name='order'),
]
