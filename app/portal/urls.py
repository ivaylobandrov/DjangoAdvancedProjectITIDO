from django.urls import path
from portal.views import csv_view

urlpatterns = [
    path("csv/", csv_view, name='csv-view'),
]