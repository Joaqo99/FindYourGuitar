from django.contrib import admin
from .models import *

# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = ("status_name", "status_id")

admin.site.register(Guitar)
admin.site.register(Search)
admin.site.register(Status, StatusAdmin)