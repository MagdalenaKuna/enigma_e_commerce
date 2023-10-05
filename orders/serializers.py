from rest_framework import serializers
from .models import Order, Address, ProductCount
from products.models import Product


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)


class ProductCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCount
        fields = ['id','product', 'count']

    def create(self, validated_data):
        return ProductCount.objects.create(**validated_data)


class OrderCreateSerializer(serializers.ModelSerializer):
    delivery_address = AddressSerializer(required=True)
    products_list = ProductCountSerializer(required=True, many=True)
    bill = serializers.SerializerMethodField()
    payment_date = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'client_fk', 'delivery_address', "products_list", 'bill', 'payment_date']

    def create(self, validated_data):
        print("validated_data: ", validated_data)
        delivery_address = Address(**validated_data["delivery_address"])
        delivery_address.save()
        products_list = ProductCount.objects.bulk_create(
            [ProductCount(**pc) for pc in validated_data["products_list"]])
        data = {"client_fk": validated_data["client_fk"], "delivery_address": delivery_address}
        bill = sum(pc.get('product').price*pc.get('count') for pc in validated_data["products_list"])
        data['bill'] = bill
        order = Order.objects.create(**data)
        order.products_list.add(*products_list)
        return order

    def get_bill(self, obj):
        return obj.bill

    def get_payment_date(self, obj):
        return obj.payment_date

    def to_representation(self, obj):
        return {"bill": obj.bill, "payment_date": obj.payment_date}


    # class OrderOutputDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['payment_date', 'bill']
