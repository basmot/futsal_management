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
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'phone_mobile', 'language')
    fieldsets = ((None, {'fields': ('user', 'email', 'phone', 'phone_mobile', 'language')}),)
    search_fields = ['user_-first_name', 'user__last_name']


class Person(models.Model):
    GENDER_CHOICES = (
        ('F', _('Female')),
        ('M', _('Male')),
        ('U', _('Unknown')))

    user         = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    gender       = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES, default='U')
    email        = models.EmailField(max_length=255, blank=True, null=True)
    phone        = models.CharField(max_length=30, blank=True, null=True)
    phone_mobile = models.CharField(max_length=30, blank=True, null=True)
    language     = models.CharField(max_length=30, null=True, choices=settings.LANGUAGES, default=settings.DEFAULT_LANGUAGE)

    def username(self):
        if self.user is None:
            return None
        return self.user.username

    def first_name(self):
        if self.user is None:
            return None
        return self.user.first_name

    def last_name(self):
        if self.user is None:
            return None
        return self.user.last_name

    def __str__(self):
        return str(self.user)


def search(user=None, gender=None, email=None, phone_mobile=None):
    queryset = Person.objects

    if user :
        queryset = queryset.filter(user=user)

    if gender :
        queryset = queryset.filter(gender=gender)

    if email :
        queryset = queryset.filter(email=email)

    if phone_mobile :
        queryset = queryset.filter(phone_mobile=phone_mobile)

    return queryset
