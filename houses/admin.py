from django.contrib import admin

# Register your models here.
from .models import House, Bedroom

admin.site.register(House)
admin.site.register(Bedroom)