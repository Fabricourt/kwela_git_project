from django.contrib import admin

from .models import Listing, Snippet 


admin.site.register(Snippet)

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'is_mvp', 'price', 'list_date', 'town', 'location', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title',  'description', 'town', 'location', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)

  
