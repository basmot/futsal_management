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
