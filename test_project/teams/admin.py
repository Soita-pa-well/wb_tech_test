from django.contrib import admin

from .models import Team, Member

EMPTY_VALUE = '---пусто--'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'team', 'time_create')
    search_fields = ('name', 'second_name', 'team')
    list_filter = ('name', 'second_name', 'team')
    empty_value_display = EMPTY_VALUE
