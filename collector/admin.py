from django.contrib import admin

from .models import Category, Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "session_id", "data", "timestamp", "created_at")


admin.site.register(Category)
admin.site.register(Event, EventAdmin)