# Generated by Django 4.2.5 on 2023-10-05 22:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_alter_order_payment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_date",
            field=models.DateField(
                default=datetime.datetime(2023, 10, 10, 22, 21, 57, 95785)
            ),
        ),
    ]