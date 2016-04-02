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


class PredictedMatchAdmin(admin.ModelAdmin):
    list_display = ('match', 'futsal_team')
    fieldsets = ((None, {'fields': ('match', 'futsal_team')}),)
    # search_fields = ['person__user__last_name']


class PredictedMatch(models.Model):
    match       = models.ForeignKey('Match')
    futsal_team = models.ForeignKey('FutsalTeam')

    def __str__(self):
        return str(self.match) + str(self.futsal_team)



def search(id=None, match=None, futsal_team=None, futsal_team_denomination=None, sport_hall_denomination=None):
    queryset = PredictedMatch.objects

    if id :
        queryset = queryset.filter(id=id)

    if match :
        queryset = queryset.filter(match=match)

    if futsal_team :
        queryset = queryset.filter(futsal_team=futsal_team)

    if futsal_team_denomination :
        queryset = queryset.filter(futsal_team__denomination__contains=futsal_team_denomination)

    if sport_hall_denomination :
        queryset = queryset.filter(match__place__denomination__contains=sport_hall_denomination)

    return queryset


def get_matchs(futsal_team):
    return [predicted_match.match for predicted_match in PredictedMatch.objects.filter(futsal_team=futsal_team)]
