from django.contrib import admin

# Register your models here.
from .models import Machine, Machine_e

admin.site.register(Machine)
admin.site.register(Machine_e)