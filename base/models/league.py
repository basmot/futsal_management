from django.db import models
from django.contrib import admin


class LeagueAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'denomination')
    fieldsets = ((None, {'fields': ('acronym', 'denomination')}),)
    search_fields = ['denomination']


class League(models.Model):
    acronym      = models.CharField(max_length=10)
    denomination = models.CharField(max_length=100)

    def __str__(self):
        return self.acronym
