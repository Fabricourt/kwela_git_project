from django.contrib import admin
from .models import Contact, Sema

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'email', 'timestamp', 'header')
  list_display_links = ('phone', 'name')
  search_fields = ('name',  'phone')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)

class SemaAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'listing', 'email', 'contact_date', 'message')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'listing')
  list_per_page = 25

admin.site.register(Sema, SemaAdmin)

