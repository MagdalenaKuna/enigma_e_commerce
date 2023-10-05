from django.db import models
import datetime
from django.conf import settings
from products.models import Product


class Address(models.Model):
    name = models.TextField()
    surname = models.TextField()
    street = models.TextField()
    street_number = models.IntegerField()
    apartment_number = models.IntegerField()
    zip_code = models.TextField()
    city = models.TextField()
    country = models.TextField()


class ProductCount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.IntegerField()


class Order(models.Model):
    @staticmethod
    def payment_days():
        return datetime.datetime.now() + datetime.timedelta(days=5)

    client_fk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    products_list = models.ManyToManyField(ProductCount)
    order_date = models.DateField(auto_now_add=True)
    payment_date = models.DateField(default=payment_days())
    bill = models.DecimalField(max_digits=10, decimal_places=2)
