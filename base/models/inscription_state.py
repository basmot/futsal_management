##############################################################################
#
# Copyright 2015-2016 Bastien Mottiaux
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
##############################################################################

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User


class InscriptionStateAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'date')
    fieldsets = ((None, {'fields': ('state','date', 'user')}),)
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



def search(user=None):
    queryset = InscriptionState.objects

    if user :
        queryset = queryset.filter(user=user)

    return queryset
