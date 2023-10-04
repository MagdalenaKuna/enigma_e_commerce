from rest_framework import generics
from .models import Order
from .serializers import OrderCreateSerializer
from accounts.permissions import SalesmanPermission, ClientPermission
from rest_framework.permissions import AllowAny


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    # permission_classes = [ClientPermission]
