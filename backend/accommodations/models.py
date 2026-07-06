from django.db import models

from trips.models import Trip


class Accommodation(models.Model):

    class Platform(models.TextChoices):
        AIRBNB = "AIRBNB", "Airbnb"
        BOOKING = "BOOKING", "Booking"
        MANUAL = "MANUAL", "Manual"

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="accommodations",
    )

    platform = models.CharField(
        max_length=20,
        choices=Platform.choices,
        default=Platform.MANUAL,
    )

    name = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    url = models.URLField(
        blank=True,
    )

    image = models.URLField(
        blank=True,
    )

    address = models.CharField(
        max_length=250,
        blank=True,
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.PositiveIntegerField(
        default=1,
    )

    price_per_night = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    cleaning_fee = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    service_fee = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    taxes = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    currency = models.CharField(
        max_length=3,
        default="ARS",
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True,
    )

    reviews = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    notes = models.TextField(
        blank=True,
    )

    @property
    def nights(self):
        return (self.check_out - self.check_in).days

    class Meta:
        ordering = ["check_in"]
        verbose_name = "Accommodation"
        verbose_name_plural = "Accommodations"

    def __str__(self):
        return f"{self.name} ({self.trip.name})"
    
    class Status(models.TextChoices):
        PLANNED = "PLANNED", "Planned"
        RESERVED = "RESERVED", "Reserved"
        PAID = "PAID", "Paid"
        CANCELLED = "CANCELLED", "Cancelled"

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNED,
    )