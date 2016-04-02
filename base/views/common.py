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

from django.shortcuts import render

from base.forms import UserEnrollmentForm
from base import models as mdl
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.views.reference import AlertLevels, new_message



def home(request):
    return render(request, "home.html")


def user_enrollment(request):
    if request.method == 'POST':
        form = UserEnrollmentForm(request.POST)
        if form.is_valid():
            user = User(username   = form.cleaned_data['username'],
                        first_name = form.cleaned_data['first_name'],
                        last_name  = form.cleaned_data['last_name'],
                        email      = form.cleaned_data['email'])
            user.save()
            person = mdl.person.Person(user       = user,
                                       gender     = form.cleaned_data['gender'],
                                       email      = form.cleaned_data['email'],
                                       phone_mobile = form.cleaned_data['phone_mobile'],
                                       language     = form.cleaned_data['language'])
            person.save()
            address = mdl.person_address.PersonAddress(person     = person,
                                                       label      = request.POST['adddress_label'],
                                                       location   = request.POST['location'],
                                                       postal_code = request.POST['postal_code'],
                                                       city        = request.POST['city'],
                                                       country     = request.POST['country'])
            inscription_state = mdl.inscription_state.InscriptionState(user=user)
            address.save()
            inscription_state.save()
            messages = [new_message(AlertLevels.SUCCESS, "Votre inscription a bien été soumise. \
                                                          Vous pourrez vous connecter une fois que l'administrateur aura validé votre inscription.")]
            return render(request, "user_enrollment.html", {'form' : form, 'GENDER_CHOICES' : mdl.person.Person.GENDER_CHOICES, 'messages' : messages})
    else:
        form = UserEnrollmentForm()
    return render(request, "user_enrollment.html", {'form' : form, 'GENDER_CHOICES' : mdl.person.Person.GENDER_CHOICES})
