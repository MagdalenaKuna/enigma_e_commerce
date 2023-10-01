from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField()
    thumbnail = models.ImageField()
    category_fk = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"

