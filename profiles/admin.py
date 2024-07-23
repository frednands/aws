from django.contrib import admin
from .models import Questions
from import_export.admin import ImportExportModelAdmin


class QuestionsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('areas_of_interest' ,'gender','nationality','emergency_contact_number','languages','availability_hours_per_week')
    search_fields =('gender','nationality','emergency_contact_number','languages','availability_hours_per_week','availability_days',)
    
    list_per_page=10
  
  
    # search_fields =('phone_number','address','created_at')
admin.site.register(Questions, QuestionsAdmin)
