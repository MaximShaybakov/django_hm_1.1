from django.contrib import admin
from .models import Advertisement, AdvertisementStatusChoices


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',
                    'status', 'creator', 'created_at',
                    'updated_at']
    list_filter = ['id', 'status', 'creator', 'created_at']
