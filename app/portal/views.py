from django.http import HttpResponse
from portal.models import CSVData


def csv_view(request):
    # Retrieve the data from the model
    data = CSVData.objects.all()

    # Create a CSV string
    csv_string = "Field1,Field2,Field3\n"  # Replace with appropriate header

    for instance in data:
        # Adjust the code below to match your model's field names
        csv_string += f"{instance.field1},{instance.field2},{instance.field3}\n"

    # Create the HTTP response with the CSV content
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    response.write(csv_string)

    return response
