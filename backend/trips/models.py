from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Trip(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_trips",
        null=True,
        blank=True,
    )

    name = models.CharField(max_length=150)

    description = models.TextField(blank=True)

    destination = models.CharField(max_length=150)

    start_date = models.DateField()

    end_date = models.DateField()

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    currency = models.CharField(
        max_length=3,
        default="ARS",
    )

    image = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self):
        return self.name

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("The start date cannot be later than the end date.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
