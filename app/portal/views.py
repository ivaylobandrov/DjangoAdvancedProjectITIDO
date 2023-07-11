from django.db.models import Avg

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
    """Endpoint to return all data related to energy prices and consumed energy."""

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


@api_view(["GET"])
def average_price_and_energy(request):
    """Endpoint to return average price and energy consumed for a given period of time."""

    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    average_price = PricesAndQuantities.objects.filter(date__range=[start_date, end_date]).aggregate(Avg("price_bgn_mwh"))
    consumed_energy = PricesAndQuantities.objects.filter(
        date__range=[start_date, end_date]).aggregate(Avg("volume_mwh"))

    return Response({"average_price": average_price["price_bgn_mwh__avg"]},
                    {"consumed_energy": consumed_energy["volume_mwh__avg"]})
