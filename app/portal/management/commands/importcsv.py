import csv
import decimal
from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from portal.models import PricesAndQuantities, BlockProduct, HourProducts


def validate_date_format(value):
    try:
        date_str = value[-5:]

        current_year = datetime.now().year
        date_with_year = f"{current_year}-{date_str}"

        validated_date = datetime.strptime(date_with_year,
                                           '%Y-%m/%d').date()

        formatted_date = validated_date.strftime('%Y-%m-%d')

        value = value.replace(date_str, formatted_date).replace(
            value[:4], '')

    except ValueError:
        raise ValidationError(
            'Invalid date format. It must be in "%a, %m/%d" format.')

    return value.strip()


def convert_price_to_decimal_number(number, decimal_separator=",",
                                    thousand_separator=" "):

    cleaned_number = number.replace(thousand_separator,
                                    '').replace(decimal_separator,
                                                '.')

    decimal_number = decimal.Decimal(cleaned_number)

    rounded_decimal = decimal_number.quantize(
        decimal.Decimal('0.00'))

    decimal_string = format(rounded_decimal, f',.2f').replace(',',
                                                              thousand_separator)

    return decimal_string


def convert_volumes_to_decimal_number(value):
    try:
        cleaned_value = value.replace(" ", "").replace(",", ".")

        decimal_number = decimal.Decimal(cleaned_value)

        return decimal_number

    except decimal.InvalidOperation:
        raise ValueError(f'Invalid decimal number: {value}')


class Command(BaseCommand):
    help = 'Import CSV data into the CSVData model'

    def handle(self, *args, **options):
        csv_file_path = "portal/csv_files/data.csv"
        with open(csv_file_path, "r") as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)

        dates = rows[2][2:]
        prices = rows[3][2:]
        volumes = rows[4][2:]
        base = rows[9][2:]
        peak = rows[10][2:]
        off_peak = rows[12][2:]
        hours = rows[8][3:]
        bgn_per_mwh = rows[9][3:]
        mwh = rows[10][3:]

        for i in range(len(dates)):
            formatted_data = validate_date_format(dates[i])
            converted_prices = convert_price_to_decimal_number(prices[i])
            converted_volumes = convert_volumes_to_decimal_number(volumes[i])

            csv_prices = PricesAndQuantities(
                date=formatted_data,
                price_bgn_mwh=converted_prices,
                volume_mwh=converted_volumes,
                # peak=peak[i],
                # off_peak=off_peak[i],
                # hour=hours[i],
                # bgn_per_mwh=bgn_per_mwh[i],
                # mwh=mwh[i]
            )
            csv_prices.save()

        self.stdout.write(self.style.SUCCESS('CSV data imported successfully.'))
