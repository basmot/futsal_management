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
from base.models import person


class SportHallAddressAdmin(admin.ModelAdmin):
    list_display = ('label', 'location', 'postal_code', 'city', 'country')
    fieldsets = ((None, {'fields': ('label', 'location', 'postal_code', 'city', 'country')}),)


class SportHallAddress(models.Model):
    label           = models.CharField(max_length=20)
    location        = models.CharField(max_length=255)
    postal_code     = models.CharField(max_length=20)
    city            = models.CharField(max_length=255)
    country         = models.CharField(max_length=255)

    def __str__(self):
        return self.location + " - " + self.postal_code + " " + self.city + " " + self.country
