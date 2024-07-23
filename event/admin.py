from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Event
# Register your models here.
    
class EventAdmin(ImportExportModelAdmin,admin.ModelAdmin):
        search_fields =('event_name','created_at','updated_at')
        list_display = ('id','event_name','created_at','updated_at')
        list_per_page=5

admin.site.register(Event,EventAdmin)