from django.db import models
import datetime
from django.conf import settings
from products.models import Product


class Address(models.Model):
    street = models.TextField()
    street_number = models.IntegerField()
    apartment_number = models.IntegerField()
    zip_code = models.TextField()
    city = models.TextField()
    country = models.TextField()


class Order(models.Model):
    client_fk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    products_list_and_numbers = models.ManyToManyField(Product)
    order_date = models.DateField(auto_now_add=True)
    payment_date = models.DateField()
    bill = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.payment_date is None:
            self.payment_date = self.order_date.date() + datetime.timedelta(days=2)
        super(Order, self).save(*args, **kwargs)

