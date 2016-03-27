from django.db import models
from django.contrib import admin
from base.models import person


class PersonAddressAdmin(admin.ModelAdmin):
    list_display = ('person', 'label', 'location', 'postal_code', 'city', 'country')
    fieldsets = ((None, {'fields': ('player', 'label', 'location', 'postal_code', 'city', 'country')}),)


class PersonAddress(models.Model):
    person      = models.ForeignKey('Person')
    label       = models.CharField(max_length=20)
    location    = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city        = models.CharField(max_length=255)
    country     = models.CharField(max_length=255)


def find_by_person(a_person):
    """ Return a list containing one or more addresses of a p. Returns None if there is no address.
    :param a_person: An instance of the class base.models.Player
    """
    return PersonAddress.objects.filter(person=a_person)
