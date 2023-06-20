import csv
import requests
from django.core.management.base import BaseCommand
from app.portal.models import CSVData


class Command(BaseCommand):
    help = "Download and upload CSV file"

    def handle(self, *args, **options):
        url = "https://ibex.bg/данни-за-пазара/пазарен-сегмент-ден-напред/пазарен-сегмент-ден-напред-2/"

        response = requests.get(url)
        response.raise_for_status()

        # Assuming the CSV file is comma-separated, adjust delimiter if needed
        reader = csv.reader(response.text.splitlines(), delimiter=',')

        # Skip header row if necessary
        # next(reader)

        # Clear existing data in the model (optional)
        CSVData.objects.all().delete()

        # Iterate over the rows and save them in the model
        for row in reader:
            # Adjust the code below to match your model's fields
            field1 = row[0]
            field2 = row[1]
            field3 = row[2]
            # ...
            # Create an instance of your model with the data from the CSV row
            instance = CSVData(field1=field1, field2=field2, field3=field3)
            instance.save()

        self.stdout.write(self.style.SUCCESS('CSV file downloaded and uploaded successfully.'))
