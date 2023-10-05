# Generated by Django 4.2.5 on 2023-10-05 22:21

from django.db import migrations, models
import django_advance_thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="thumbnail",
            field=django_advance_thumbnail.fields.AdvanceThumbnailField(
                blank=True, null=True, upload_to="images/thumbnails/"
            ),
        ),
    ]
