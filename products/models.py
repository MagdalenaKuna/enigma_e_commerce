from django.db import models
from django_advance_thumbnail import AdvanceThumbnailField

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    thumbnail = AdvanceThumbnailField(source_field='picture', upload_to='images/thumbnails/', null=True, blank=True,
                                      size=(200, 200))
    category_fk = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"

