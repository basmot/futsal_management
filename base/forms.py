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

from django import forms
from django.forms import ModelForm
from base import models as mdl
from django.core.validators import validate_email
from django.contrib.auth.models import User


class FutsalTeamForm(forms.Form):
    denomination = forms.CharField(min_length=3, strip=True)


class MatchsForm(forms.Form):
    futsal_team_denomination = forms.CharField(min_length=2, strip=True, required=False)
    sport_hall_denomination  = forms.CharField(min_length=2, strip=True, required=False)


class UserEnrollmentForm(forms.Form):
    username    = forms.CharField(min_length=9)
    password1   = forms.CharField(widget=forms.PasswordInput, min_length=9)
    password2   = forms.CharField(widget=forms.PasswordInput, min_length=9)
    first_name  = forms.CharField()
    last_name   = forms.CharField()
    gender      = forms.CharField(required=False)
    email       = forms.EmailField()
    phone       = forms.CharField(required=False)
    phone_mobile= forms.CharField(strip=True)
    language    = forms.CharField(required=False)

    class Meta:
        model = mdl.person.Person
        fields = ['gender', 'email', 'phone', 'phone_mobile', 'language']

    def is_valid(self):
        valid = super(UserEnrollmentForm, self).is_valid()
        if not valid :
            return valid

        if self.cleaned_data['password1'] and self.cleaned_data['password2'] :
            if self.cleaned_data['password1'] != self.cleaned_data['password2'] :
                error = 'Les deux mots de passe entrés doivent être exactement les mêmes.'
                self._errors['password1'] = error
                self._errors['password2'] = error
                return False

        users = User.objects.filter(username=self.cleaned_data['username'])
        if users.count() > 0 :
            self._errors['username'] = 'Ce login est déjà utilisé.'
            return False

        try:
            validate_email(self.cleaned_data['email'])
        except forms.ValidationError:
            self._errors['email'] = "L'email entré n'est pas valide."
            return False

        persons = mdl.person.search(email=self.cleaned_data['email'])
        if persons.count() > 0 :
            self._errors['email'] = 'Cet email est déjà utilisé'
            return False

        phone_mobile = self.cleaned_data['phone_mobile']
        phone_mobile = phone_mobile.replace(" ", "")
        self.cleaned_data['phone_mobile'] = phone_mobile
        if len(phone_mobile) != 13 :
            self._errors['phone_mobile'] = "Le numéro entré n'est pas valide."
            return False
        persons = mdl.person.search(phone_mobile=phone_mobile)
        if persons.count() > 0 :
            self._errors['phone_mobile'] = 'Ce numéro de téléphone existe déjà.'
            return False

        return True
