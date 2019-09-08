from django.contrib import admin
from database.models import News, Team, Player

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'published', 'source', 'url', 'title', 'content_raw', 'content_display', 'image')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'short_name', 'full_en_name', 'joined', 'area', 'arena')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name', 'team')

admin.site.register(News, NewsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
