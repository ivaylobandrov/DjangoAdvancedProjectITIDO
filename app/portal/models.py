from django.db import models


class CSVData(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)

    def __str__(self):
        return f"CSVData: {self.field1}, {self.field2}, {self.field3}"

    class Meta:
        db_table = 'csv_data'
