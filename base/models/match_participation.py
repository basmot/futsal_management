from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class MatchParticipationAdmin(admin.ModelAdmin):
    list_display = ('match', 'person', 'position')
    fieldsets = ((None, {'fields': ('match', 'person', 'position')}),)
    # search_fields = ['person__user__last_name']
    list_filter = ('position',)


class MatchParticipation(models.Model):
    POSITIONS = (
            ('co', _('Coach')),
            ('ca', _('Captain')),
            ('d', _('Deleguee')),
            ('k', _('Keeper')),
            ('p', _('Player')),
            ('r', _('Referee'))
    )

    match       = models.ForeignKey('Match')
    person      = models.ForeignKey('Person')
    position    = models.CharField(max_length=2, choices=POSITIONS)


    def __str__(self):
        return self.person + self.match
