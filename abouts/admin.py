from django.contrib import admin

# Register your models here.
from .models import About, Proposal, Howtojoin, Faq


admin.site.register(About)
admin.site.register(Proposal)
admin.site.register(Howtojoin)
admin.site.register(Faq)
