from django.contrib import admin

from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "destination",
        "start_date",
        "end_date",
        "owner",
        "budget",
        "currency",
    )

    search_fields = (
        "name",
        "destination",
        "owner__username",
        "owner__email",
    )

    list_filter = (
        "currency",
        "start_date",
        "end_date",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Información general",
            {
                "fields": (
                    "owner",
                    "name",
                    "description",
                    "destination",
                )
            },
        ),
        (
            "Planificación",
            {
                "fields": (
                    "start_date",
                    "end_date",
                    "budget",
                    "currency",
                )
            },
        ),
        (
            "Imagen",
            {
                "fields": (
                    "image",
                )
            },
        ),
        (
            "Auditoría",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )