from django.db import models
from django.contrib import admin
from base.models import person


class SportHallAddressAdmin(admin.ModelAdmin):
    list_display = ('sport_hall', 'label', 'location', 'postal_code', 'city', 'country')
    fieldsets = ((None, {'fields': ('sport_hall', 'label', 'location', 'postal_code', 'city', 'country')}),)


class SportHallAddress(models.Model):
    sport_hall      = models.ForeignKey('SportHall')
    label           = models.CharField(max_length=20)
    location        = models.CharField(max_length=255)
    postal_code     = models.CharField(max_length=20)
    city            = models.CharField(max_length=255)
    country         = models.CharField(max_length=255)

    def __str__(self):
        return location + " - " + postal_code + " " + city + country


def find_by_sport_hall(a_sport_hall):
    """ Return a list containing one or more addresses of a sporthall. Returns None if there is no address.
    :param a_sport_hall: An instance of the class base.models.SportHall
    """
    return PersonAddress.objects.filter(sport_hall=a_sport_hall)
