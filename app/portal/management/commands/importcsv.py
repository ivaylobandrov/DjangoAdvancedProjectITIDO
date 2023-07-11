import csv
import decimal
from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from portal.models import PricesAndQuantities, BlockProduct, HourProducts


def validate_date_format(value):
    """ Function to validate the date format."""

    try:
        date_str = value[-5:]

        current_year = datetime.now().year
        date_with_year = f"{current_year}-{date_str}"

        validated_date = datetime.strptime(date_with_year, "%Y-%m/%d").date()

        formatted_date = validated_date.strftime("%Y-%m-%d")

        value = value.replace(date_str, formatted_date).replace(value[:4], "")

    except ValueError:
        raise ValidationError('Invalid date format. It must be in "%a, %m/%d" format.')

    return value.strip()


def convert_price_to_decimal_number(
    number, decimal_separator=",", thousand_separator=" "
):
    """Function to convert the price to decimal number since the price in the csv files is in different format."""
    cleaned_number = number.replace(thousand_separator, "").replace(
        decimal_separator, "."
    )

    decimal_number = decimal.Decimal(cleaned_number)

    rounded_decimal = decimal_number.quantize(decimal.Decimal("0.00"))

    decimal_string = format(rounded_decimal, f",.2f").replace(",", thousand_separator)

    return decimal_string


def convert_volumes_to_decimal_number(value):
    """Function to convert the volume to decimal number since the volume in the csv files is in different format."""
    try:
        cleaned_value = value.replace(" ", "").replace(",", ".")

        decimal_number = decimal.Decimal(cleaned_value)

        return decimal_number

    except decimal.InvalidOperation:
        raise ValueError(f"Invalid decimal number: {value}")


class Command(BaseCommand):
    """Django custom command to import csv data into the database."""

    help = "Import CSV data into the CSVData model"

    def handle(self, *args, **options):
        csv_file_path = "portal/csv_files/data.csv"
        with open(csv_file_path, "r") as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)

        dates_prices = rows[2][2:]
        prices = rows[3][2:]
        volumes = rows[4][2:]
        dates_block_products = rows[8][2:]
        base_price_bgn_mwh = rows[9][2:]
        peak_price_bgn_mwh = rows[10][2:]
        off_peak_price_bgn_mwh = rows[12][2:]
        dates_hour_products = rows[16][2:]
        slots = rows[17:2]
        bgn_per_mwh = rows[9][3:]
        # mwh = rows[10][3:]

        for i in range(len(dates_prices)):
            formatted_date_prices = validate_date_format(dates_prices[i])
            converted_prices = convert_price_to_decimal_number(prices[i])
            converted_volumes = convert_volumes_to_decimal_number(volumes[i])

            formatted_date_block_products = validate_date_format(
                dates_block_products[i]
            )
            converted_prices_block_products = convert_price_to_decimal_number(
                base_price_bgn_mwh[i]
            )
            converted_prices_peak_price_bgn_mwh = convert_price_to_decimal_number(
                peak_price_bgn_mwh[i]
            )
            converted_prices_off_peak_price_bgn_mwh = convert_price_to_decimal_number(
                off_peak_price_bgn_mwh[i]
            )

            # formatted_date_hour_products = validate_date_format(dates_hour_products[i])
            # converted_prices_bgn_per_mwh = convert_price_to_decimal_number(bgn_per_mwh[i])

            csv_prices = PricesAndQuantities(
                date=formatted_date_prices,
                price_bgn_mwh=converted_prices,
                volume_mwh=converted_volumes,
            )

            block_products = BlockProduct(
                date=formatted_date_block_products,
                base_price_bgn_mwh=converted_prices_block_products,
                peak_price_bgn_mwh=converted_prices_peak_price_bgn_mwh,
                off_peak_price_bgn_mwh=converted_prices_off_peak_price_bgn_mwh,
            )

            # hour_products = HourProducts(
            #     date=formatted_date_hour_products,
            #     timeslot=slots,
            #     # price_bgn_mwh=converted_prices_bgn_per_mwh,
            #     # volume_mwh="",
            # )

            # print("DATES: ", formatted_date_hour_products)
            # print("PRICE PER MW: ", bgn_per_mwh)

            csv_prices.save()
            block_products.save()
            # hour_products.save()

        self.stdout.write(self.style.SUCCESS("CSV data imported successfully."))
