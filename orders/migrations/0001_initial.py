# Generated by Django 4.2.5 on 2023-10-01 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("street", models.TextField()),
                ("street_number", models.IntegerField()),
                ("apartment_number", models.IntegerField()),
                ("zip_code", models.TextField()),
                ("city", models.TextField()),
                ("country", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_date", models.DateField(auto_now_add=True)),
                ("payment_date", models.DateField()),
                ("bill", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "delivery_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "products_list_and_numbers",
                    models.ManyToManyField(to="products.product"),
                ),
            ],
        ),
    ]