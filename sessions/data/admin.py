from django.contrib import admin
from .models import DataModel
import requests


# admin.site.register(DataModel)
@admin.action(description="Call Data Api")
def call_data_api(self, request, queryset):
    data = requests.get("http://localhost:8000/api/data/")
    self.message_user(request, "%s" % data.text)


@admin.action(description="Call Session Api")
def call_session_api(self, request, queryset):
    data = requests.get("http://localhost:8000/api/session/")
    self.message_user(request, "%s" % data.text)


@admin.register(DataModel)
class DataAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "request_data",
        "request_number",
        "created_at",
        "updated_at",
        "session_value",
        "session_create_time",
        "activity_time",
    ]
    ordering = ('request_number',)
    search_fields = ('request_data', 'request_number')
    actions = [call_data_api, call_session_api]

