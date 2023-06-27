from django.shortcuts import render
import csv


def render_csv(request):
    csv_file_path = "portal/csv_files/data.csv"

    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        csv_data = list(reader)

    # Pass the CSV data to the template
    return render(request, 'render_csv.html', {'csv_data': csv_data})
