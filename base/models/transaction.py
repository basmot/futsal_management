from django.db import models
from django.contrib import admin
from django.utils import timezone


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'note')
    # fieldsets = ((None, {'fields': ('title',)}),)
    search_fields = ['amount','date']


class Transaction(models.Model):
    amount           = models.IntegerField()
    date             = models.DateTimeField(default=timezone.now)
    note             = models.CharField(max_length=150)


    def __str__(self):
        return self.date + " - " + amount + "€"
