from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.category = validated_data.get('category_fk', instance.category)
