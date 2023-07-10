from django.db import models


class PricesAndQuantities(models.Model):
    """PricesAndQuantities model."""

    __tablename__ = "pricesandquantities"

    date = models.DateField(null=True, blank=True)
    price_bgn_mwh = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    volume_mwh = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )


class BlockProduct(models.Model):
    """BlockProduct model."""

    __tablename__ = "blockproduct"

    date = models.DateField(null=True, blank=True)
    base_price_bgn_mwh = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    peak_price_bgn_mwh = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    off_peak_price_bgn_mwh = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )


class HourProducts(models.Model):
    """HourProducts model."""

    __tablename__ = "hourproducts"

    date = models.DateField(null=True, blank=True)
    timeslot = models.CharField(max_length=10, null=True, blank=True)
    price_bgn_mwh = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    volume_mwh = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
