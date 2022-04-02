from django.contrib import admin

from .models import Category, Event, EventError


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "session_id", "data", "timestamp", "created_at")


class EventErrorAdmin(admin.ModelAdmin):
    list_display = ("message", "data", "created_at")


admin.site.register(Category)
admin.site.register(Event, EventAdmin)
admin.site.register(EventError, EventErrorAdmin)