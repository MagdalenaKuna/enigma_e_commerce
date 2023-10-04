from rest_framework import serializers
from .models import Order, Address, ProductCount


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)


class ProductCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCount
        fields = '__all__'

    def create(self, validated_data):
        return ProductCount.objects.create(**validated_data)


class OrderCreateSerializer(serializers.ModelSerializer):
    delivery_address = AddressSerializer(required=True)
    products_list = ProductCountSerializer(required=True)

    class Meta:
        model = Order
        fields = ['id', 'client_fk', 'delivery_address', 'products_list']

    def create(self, validated_data):
        print("validated_data: ", validated_data)
        delivery_address = Address(**validated_data["delivery_address"])
        delivery_address.save()
        products_list = ProductCount(**validated_data["products_list"])
        products_list.save()
        return Order.objects.create({"client_fk": validated_data["client_fk"],
                                     "delivery_address": delivery_address, "products_list": products_list})


class OrderRestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_date', 'bill']
