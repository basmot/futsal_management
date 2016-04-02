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
from django.contrib.auth.views import login as django_login
from django.contrib.auth import authenticate
from base.views.reference import AlertLevels, new_message



def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print("user====" + str(user))
        if user :
            inscr_states = mdl.inscription_state.search(user=user)
            if inscr_states :
                inscr_state = inscr_states[0] #inscr_state is a queryset
                STATES = mdl.inscription_state.InscriptionState.STATES
                if inscr_state.state == STATES[0][0] :
                    message = new_message(AlertLevels.WARNING, "Votre login n'a pas encore été validé par l'administrateur du site.\
                                                                Veuillez attendre que ce dernier valide votre inscription. Vous pourrez\
                                                                ensuite vous identifier tout à fait normalement.")
                    return render(request, "registration/login.html", {'messages' : [message]})
                elif inscr_state.state == STATES[2][0] :
                    message = new_message(AlertLevels.WARNING, "Votre demande d'inscription a été refusée ou votre compte a été temporairement désactivé. \
                                                                Vous ne saurez donc pas vous connecter. ")
                    return render(request, "registration/login.html", {'messages' : [message]})
            person = mdl.person.search(user=user)[0]
            accounts = mdl.account.search(owner=person)
            if accounts :
                request.session['balance'] = accounts[0].balance
            else :
                account = mdl.account.Account()
                account.save()
                request.session['balance'] = 0

    return django_login(request)


def user_enrollment(request):
    if request.method == 'POST':
        form = UserEnrollmentForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                        first_name = form.cleaned_data['first_name'],
                        password   = form.cleaned_data['password2'],
                        last_name  = form.cleaned_data['last_name'],
                        email      = form.cleaned_data['email'])
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
