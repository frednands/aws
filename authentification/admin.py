from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import User,Position
# Register your models here.
class UserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields =('username','first_name','last_name')
    list_display = ('username','email','first_name','last_name','is_staff')
    list_per_page=5
    
class PositionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields =('position_name','created_at','owner')
    list_display = ('position_name','owner')
    list_per_page=3
    

admin.site.register(User,UserAdmin)
admin.site.register(Position,PositionAdmin)