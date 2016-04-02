from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'place', 'match_type')
    fieldsets = ((None, {'fields': ('place', 'match_type', 'date')}),)
    search_fields = ['place__denomination']
    list_filter = ('match_type',)


class Match(models.Model):
    MATCH_TYPES = (
            ('FRIENDLY', _('Friendly')),
            ('TRAINING', _('Training')),
            ('OFFICIAL', _('Official'))
    )

    date        = models.DateTimeField()
    place       = models.ForeignKey('SportHall')
    match_type  = models.CharField(max_length=15, choices=MATCH_TYPES)

    @property
    def present_futsal_teams(self):
        return [pm.futsal_team for pm in self.predictedmatch_set.filter(match=self)]

    def __str__(self):
        return str(self.date) + str(self.place)


def search(id=None):
    queryset = Match.objects

    if id :
        queryset = queryset.filter(id=id)

    return queryset
