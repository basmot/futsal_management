from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User


class InscriptionStateAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'date')
    fieldsets = ((None, {'fields': ('state','date')}),)
    search_fields = ['user__last_name', 'user__first_name']
    list_filter = ('state',)


class InscriptionState(models.Model):
    STATES = (
        ('PENDING', _('Pending')), # En attente
        ('ACCEPTED', _('Accepted')),
        ('REFUSED', _('Refused')))

    user  = models.ForeignKey(User)
    state = models.CharField(max_length=30, choices=STATES, default="PENDING")
    date  = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.user) + " " + self.state
