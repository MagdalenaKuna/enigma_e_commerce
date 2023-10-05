from rest_framework import views
from rest_framework.response import Response
from .serializers import ProductStatisticSerializer
from django.utils.dateparse import parse_datetime
from accounts.permissions import SalesmanPermission


class ProductStatistics(views.APIView):
    permission_classes = [SalesmanPermission]

    def get(self, request):
        query_data = {"date_from": parse_datetime(request.query_params["date_from"]),
                      "date_to": parse_datetime(request.query_params["date_to"]),
                      "product_counter": int(request.query_params["product_counter"])}
        results = ProductStatisticSerializer(data=query_data)
        if results.is_valid():
            return Response(results.the_most_common_products())

        return Response(status=400)
