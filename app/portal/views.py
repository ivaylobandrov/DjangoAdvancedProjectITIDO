from rest_framework.response import Response
from rest_framework.decorators import api_view
import csv

from portal.serializers import CSVSerializer


@api_view(['GET'])
def render_csv(request):
    csv_file_path = "portal/csv_files/data.csv"

    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        csv_data = list(reader)

    # Serialize the CSV data
    serializer = CSVSerializer({'csv_data': csv_data})

    # Return the serialized data
    return Response(serializer.data)
