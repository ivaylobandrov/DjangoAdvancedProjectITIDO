from rest_framework import serializers


class CSVSerializer(serializers.Serializer):
    csv_data = serializers.ListField(child=serializers.ListField())
