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
