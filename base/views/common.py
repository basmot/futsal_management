from django.shortcuts import render

from base.forms import UserEnrollmentForm
from base import models as mdl
from django.contrib.auth.models import User

# Create your views here.

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
            messages = [{'level'   : 'alert-success',
                         'message' : "Votre inscription a bien été soumise. \
                                      Vous pourrez vous connecter une fois que l'administrateur aura validé votre inscription."}]
            return render(request, "user_enrollment.html", {'form' : form, 'GENDER_CHOICES' : mdl.person.Person.GENDER_CHOICES, 'messages' : messages})
    else:
        form = UserEnrollmentForm()
        print(str(form))
    return render(request, "user_enrollment.html", {'form' : form, 'GENDER_CHOICES' : mdl.person.Person.GENDER_CHOICES})
