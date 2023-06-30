from rest_framework.response import Response
from rest_framework.decorators import api_view

from portal.models import PricesAndQuantities, BlockProduct, HourProducts
from portal.serializers import (
    PricesAndQuantitiesSerializer,
    BlockProductSerializer,
    HourProductsSerializer,
)


@api_view(["GET"])
def render_csv(request):
    prices_data = PricesAndQuantities.objects.all()
    block_products_data = BlockProduct.objects.all()
    hour_products = HourProducts.objects.all()

    prices_serializer = PricesAndQuantitiesSerializer(prices_data, many=True)
    block_product_serializer = BlockProductSerializer(block_products_data, many=True)
    hour_products_serializer = HourProductsSerializer(hour_products, many=True)

    response_data = {
        "prices_data": prices_serializer.data,
        "block_products_data": block_product_serializer.data,
        "hour_products_data": hour_products_serializer.data,
    }

    return Response(response_data)
