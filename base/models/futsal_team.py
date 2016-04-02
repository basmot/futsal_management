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


class FutsalTeamAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'denomination')
    fieldsets = ((None, {'fields': ('acronym','denomination', 'account')}),)
    search_fields = ['denomination']


class FutsalTeam(models.Model):
    acronym             = models.CharField(max_length=10)
    denomination        = models.CharField(max_length=100)
    account             = models.ForeignKey('Account')

    @property
    def number_of_players(self):
        return self.futsalteamenrollment_set.filter(state_enrollment='ACCEPTED').count()

    def __str__(self):
        return self.acronym

def search(id=None, acronym=None, denomination=None):
    queryset = FutsalTeam.objects

    if id :
        queryset = queryset.filter(id=id)

    if acronym :
        queryset = queryset.filter(acronym__contains=acronym)

    if denomination :
        queryset = queryset.filter(denomination__contains=denomination)

    return queryset
