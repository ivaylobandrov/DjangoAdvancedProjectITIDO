from celery import shared_task
from django.core.management import call_command


@shared_task
def download_csv_task():
    call_command('downloadcsv')

@shared_task
def import_csv_task():
    call_command('importcsv')
