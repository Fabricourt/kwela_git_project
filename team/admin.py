from django.contrib import admin
from .models import Team, Teamhead


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'phone', 'email', 'timestamp')
admin.site.register(Team, TeamAdmin)

class TeamheadAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo_short_name', 'motivational_statement')
admin.site.register(Teamhead, TeamheadAdmin)