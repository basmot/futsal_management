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
