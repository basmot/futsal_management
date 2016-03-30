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
