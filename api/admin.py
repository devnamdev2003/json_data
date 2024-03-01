from django.contrib import admin
from .models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    search_fields = ['json_data']
    list_filter = ['json_data']
    list_display = ['id', 'json_data']
