from django.contrib import admin

# Register your models here.
from .models import Truck, Truck_type

admin.site.register(Truck)
admin.site.register(Truck_type)
