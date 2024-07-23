from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_at','updated_at',)
    search_fields = ('title','created_at',)
    list_per_page = 5
admin.site.register(Post, PostAdmin)
