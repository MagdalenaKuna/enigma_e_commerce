from django.db.models import Sum
from rest_framework import serializers
from orders.models import Order, ProductCount
from products.models import Product

class ProductStatisticSerializer(serializers.Serializer):
    date_from = serializers.DateTimeField()
    date_to = serializers.DateTimeField()
    product_counter = serializers.IntegerField()

    def the_most_common_products(self):
        orders = Order.objects.filter(order_date__range=
                                      [self.validated_data["date_from"],
                                       self.validated_data["date_to"]])
        ids = [product["products_list"] for product in orders.values("products_list")
               if product["products_list"] is not None]
        product_counts = ProductCount.objects.filter(id__in=ids)\
                                             .values("product")\
                                             .annotate(sum=Sum("count"))\
                                             .order_by('-sum')[:self.validated_data['product_counter']]

        return [
            {
                "product": Product.objects.filter(pk=product_counts[0]["product"]).values().first(),
                "sum": pc["sum"]
            } for pc in product_counts
        ]
