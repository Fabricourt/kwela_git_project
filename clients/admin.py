from django.contrib import admin
from clients.models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'email', 'phone', 'is_published')
    list_filter =( 'first_name', 'last_name',)
    list_editable = ('is_published',)
    list_per_page = 25
admin.site.register(Client, ClientAdmin)


