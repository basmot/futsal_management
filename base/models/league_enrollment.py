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


class LeagueEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('league', 'futsal_team', 'division', 'category')
    fieldsets = ((None, {'fields': ('league','futsal_team', 'home_sport_hall', 'division')}),)
    search_fields = ['league__acronym', 'futsal_team__denomination']
    list_filter = ('category',)


class LeagueEnrollment(models.Model):
    DIVISIONS = (
            ('D1', _('Division 1 (National)')),
            ('D2', _('Division 2 (National)')),
            ('D3', _('Division 3 (National)')),
            ('P1', _('Provincial 1')),
            ('P2', _('Provincial 2')),
            ('P3', _('Provincial 3')),
            ('P4', _('Provincial 4')),
            ('P5', _('Provincial 5')))

    CATEGORIES = (
            ('J', _('Junior')),
            ('S', _('Senior')),
            ('V', _('Veteran')),
            ('F', _('Woman'))
    )

    league           = models.ForeignKey('League')
    futsal_team      = models.ForeignKey('FutsalTeam')
    home_sport_hall  = models.ForeignKey('SportHall')
    division         = models.CharField(max_length=2, blank=True, null=True, choices=DIVISIONS)
    category         = models.CharField(max_length=1, blank=True, null=True, choices=CATEGORIES)
    date             = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.league) + str(self.futsal_team)
