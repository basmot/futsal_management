from django.db import models
from django.contrib import admin


class FutsalTeamAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'denomination')
    fieldsets = ((None, {'fields': ('acronym','denomination')}),)
    search_fields = ['denomination']


class FutsalTeam(models.Model):
    acronym             = models.CharField(max_length=10)
    denomination        = models.CharField(max_length=100)
    account             = models.ForeignKey('Account')
    match_participation = models.ForeignKey('MatchParticipation')

    def __str__(self):
        return self.acronym
