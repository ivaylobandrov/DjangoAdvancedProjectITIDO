from rest_framework import serializers
from portal.models import PricesAndQuantities, BlockProduct, HourProducts


class PricesAndQuantitiesSerializer(serializers.ModelSerializer):
    """PricesAndQuantities serializer"""

    class Meta:
        model = PricesAndQuantities
        fields = "__all__"


class BlockProductSerializer(serializers.ModelSerializer):
    """BlockProduct serializer."""

    class Meta:
        model = BlockProduct
        fields = "__all__"


class HourProductsSerializer(serializers.ModelSerializer):
    """HourProducts serializer"""

    class Meta:
        model = HourProducts
        fields = "__all__"
