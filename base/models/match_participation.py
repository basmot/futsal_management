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
    futsal_team = models.ForeignKey('FutsalTeam', null = True, blank = True)
    position    = models.CharField(max_length=2, choices=POSITIONS)


    def __str__(self):
        return str(self.person) + str(self.match)



def search(id=None, match=None, futsal_team=None):
    queryset = MatchParticipation.objects

    if id :
        queryset = queryset.filter(id=id)

    if match :
        queryset = queryset.filter(match=match)

    if futsal_team :
        queryset = queryset.filter(futsal_team=futsal_team)

    return queryset


def delete(match, person, futsal_team):
    return MatchParticipation.objects.filter(match=match, person=person, futsal_team=futsal_team).delete()
