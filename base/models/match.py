from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'place', 'match_type')
    fieldsets = ((None, {'fields': ('place', 'match_type')}),)
    search_fields = ['place__denomination']
    list_filter = ('match_type',)


class Match(models.Model):
    MATCH_TYPES = (
            ('FRIENDLY', _('Friendly')),
            ('TRAINING', _('Training')),
            ('OFFICIAL', _('Official'))
    )

    date        = models.DateTimeField(default=timezone.now)
    place       = models.ForeignKey('SportHall')
    match_type  = models.CharField(max_length=15, choices=MATCH_TYPES)


    def __str__(self):
        return self.date + self.place
