from django.contrib import admin

# Register your models here.
from .models import (About)
from .models import (Proposal)

admin.site.register(About)
admin.site.register(Proposal)