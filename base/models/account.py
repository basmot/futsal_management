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


class AccountAdmin(admin.ModelAdmin):
    list_display = ('balance', 'bank_name', 'owner')
    fieldsets = ((None, {'fields': ('balance','bank_name', 'owner')}),)
    search_fields = ['owner__user__last_name', 'owner__user__first_name',]


class Account(models.Model):
    balance      = models.IntegerField(default=0)
    bank_name    = models.CharField(max_length=100, blank = True, null = True)
    owner        = models.ForeignKey('Person', null = True)


    def __str__(self):
        return str(self.owner.user) + " " + str(self.id)


def search(owner=None):
    queryset = Account.objects

    if owner :
        queryset = queryset.filter(owner=owner)

    return queryset
