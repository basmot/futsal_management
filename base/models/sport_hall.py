from django.db import models
from django.contrib import admin


class SportHallAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'denomination', 'address')
    fieldsets = ((None, {'fields': ('acronym', 'denomination', 'address')}),)
    search_fields = ['denomination']


class SportHall(models.Model):
    acronym      = models.CharField(max_length=10)
    denomination = models.CharField(max_length=100)
    address      = models.ForeignKey('SportHallAddress')

    def __str__(self):
        return self.acronym
