from rest_framework import serializers
from portal.models import PricesAndQuantities, BlockProduct, HourProducts


class PricesAndQuantitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricesAndQuantities
        fields = "__all__"


class BlockProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockProduct
        fields = "__all__"


class HourProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourProducts
        fields = "__all__"
