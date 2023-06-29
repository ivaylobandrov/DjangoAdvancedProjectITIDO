from rest_framework.response import Response
from rest_framework.decorators import api_view

from portal.models import PricesAndQuantities, BlockProduct, HourProducts
from portal.serializers import PricesAndQuantitiesSerializer, BlockProductSerializer, HourProductsSerializer


@api_view(['GET'])
def render_csv(request):

    csv_data = PricesAndQuantities.objects.all()

    serializer = PricesAndQuantitiesSerializer(csv_data, many=True)

    return Response(serializer.data)
