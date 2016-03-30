from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class FutsalTeamEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('person', 'futsal_team', 'state_enrollment', 'is_admin')
    fieldsets = ((None, {'fields': ('person','futsal_team', 'state_enrollment', 'is_admin')}),)
    search_fields = ['person__user__first_name', 'person__user__last_name', 'person__login']
    list_filter = ('is_admin', 'state_enrollment')


class FutsalTeamEnrollment(models.Model):
    STATES = (
        ('PENDING', _('Pending')), # En attente
        ('ACCEPTED', _('Accepted')),
        ('REFUSED', _('Refused')))

    person           = models.ForeignKey('Person')
    futsal_team      = models.ForeignKey('FutsalTeam')
    state_enrollment = models.CharField(max_length=30, choices=STATES, default="PENDING")
    is_admin         = models.BooleanField(default=False)
    date_enrollment  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.person) + str(self.futsal_team)

def search(futsal_team=None):
    queryset = FutsalTeamEnrollment.objects

    if futsal_team :
        queryset = queryset.filter(futsal_team=futsal_team)

    return queryset
