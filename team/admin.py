from django.contrib import admin
from .models import Team, Teamhead
import csv


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_header', 'team', 'phone', 'email', 'facebook', 'twitter', 'linkedin', 'instagram', 'timestamp', 'is_published')
    list_display_links = ('phone', 'team')
    search_fields = ('team',  'phone')
    list_editable = ('is_published',)
    list_per_page = 25
admin.site.register(Team, TeamAdmin)

class TeamheadAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo_short_name', 'motivational_statement')
admin.site.register(Teamhead, TeamheadAdmin)


"""
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin, ExportCsvMixin):

    readonly_fields = [..., "team_header"]

    def team_header(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
    )
"""