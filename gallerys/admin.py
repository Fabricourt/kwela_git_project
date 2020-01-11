from django.contrib import admin
from .models import Photo



class PhotoAdmin(admin.ModelAdmin):
  list_display = ('title', 'name')
  list_display_links = ('title', 'name')
  search_fields = ('name', 'title')
  list_per_page = 25

admin.site.register(Photo, PhotoAdmin)

