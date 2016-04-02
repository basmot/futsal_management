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


class AccountTransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction')


class AccountTransaction(models.Model):
    account      = models.ForeignKey('Account')
    transaction  = models.ForeignKey('Transaction')

    def __str__(self):
        return self.account + " - " + transaction
