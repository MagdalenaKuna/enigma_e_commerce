from rest_framework import generics
from .models import Order
from .serializers import OrderCreateSerializer
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from accounts.permissions import SalesmanPermission, ClientPermission


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    # permission_classes = [ClientPermission]

    def send_email(self, request):
        subject = "Order confirmation"
        message = "Thank you for your order."
        from_email = "admin@example.com"
        to_email = [request.user.email]
        try:
            send_mail(subject, message, from_email, to_email)
        except BadHeaderError:
            print("Invalid header found.")

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        self.send_email(request)
        return response



class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    # permission_classes = [ClientPermission]
