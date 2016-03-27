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


    def __str__(self):
        return self.user
