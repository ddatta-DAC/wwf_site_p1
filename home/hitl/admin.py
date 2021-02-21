from django.contrib import admin

from .models import Epoch


@admin.register(Epoch)
class EpochAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'date')
    list_filter = ('date',)
    search_fields = ('name',)
