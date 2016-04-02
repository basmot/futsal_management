from django.shortcuts import render

from base.forms import UserEnrollmentForm, FutsalTeamForm, MatchsForm
from base import models as mdl
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


AlertLevels = type(
    "AlertLevel",
    (),
    {
         'ERROR' : 'alert-danger',
         'WARNING' : 'alert-warning',
         'INFO' : 'alert-info',
         'SUCCESS' : 'alert-success'
    })


def new_message(level, content):
    """
    Construit un dictionnaire sous la forme
    {'level' = 'alert-info', # Peut être aussi 'alert-success', 'alert-danger'...
     'content' = "The message's content"}
    """
    return {'level' : level, 'content' : content}

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


@login_required
def futsal_teams(request):
    # futsal_teams = mdl.futsal_team.FutsalTeam.objects.all()
    return render(request, "futsal_teams.html")


@login_required
def futsal_team(request, futsal_team_id):
    if futsal_team_id:
        futsal_team = mdl.futsal_team.search(id=futsal_team_id)[0]
        matchs = mdl.predicted_match.get_matchs(futsal_team=futsal_team)
        futsal_team_enrollments = mdl.futsal_team_enrollment.search(futsal_team=futsal_team)
        persons = [fte.person for fte in futsal_team_enrollments]
    else :
        futsal_team = None
        matchs = None
        persons = None
        message = new_message(AlertLevels.ERROR, "Votre demande de recrutement n'a pas aboutie ; l'équipe sélectionnée n'existe pas/plus.")
    return render(request, "futsal_team.html", {'futsal_team' : futsal_team,
                                                'account' : futsal_team.account,
                                                'matchs' : matchs,
                                                'persons' : persons})


@login_required
def futsal_teams_search(request):
    # form = FutsalTeamForm(request.POST)
    denomination = request.POST['denomination']
    if denomination :
        futsal_teams = mdl.futsal_team.search(denomination=denomination)
    else :
        futsal_teams = mdl.futsal_team.FutsalTeam.objects.all()
    return render(request, "futsal_teams.html", {'futsal_teams' : futsal_teams})


@login_required
def futsal_team_enrollment(request, futsal_team_id):
    if futsal_team_id:
        futsal_team = mdl.futsal_team.search(id=futsal_team_id)[0]
        enrollments = mdl.futsal_team_enrollment.search(futsal_team=futsal_team)
        if len(enrollments) > 0 : # Déjà inscrit à l'équipe
            enrollment = enrollments[0]
            enr_states = mdl.futsal_team_enrollment.FutsalTeamEnrollment.STATES
            if enrollment.state_enrollment == enr_states[0][0] :
                msg = "Vous avez déjà demandé d'intégrer cette équipe, votre demande est toujours \
                       en attente de confirmation du gérant de l'équipe " + futsal_team.acronym + "."
            elif enrollment.state_enrollment == enr_states[1][0] :
                msg = "Vous faites déjà partie de l'équipe " + futsal_team.acronym + "."
            else :
                msg = "Vous avez déjà demandé à intégrer l'équipe " + futsal_team.acronym + ", mais \
                       votre candidature a été refusée."
            message = new_message(AlertLevels.WARNING, msg)
        else : # Aucune isncription à cette équipe
            person = mdl.person.search(user=request.user)[0]
            enrollment = mdl.futsal_team_enrollment.FutsalTeamEnrollment(person=person, futsal_team=futsal_team)
            enrollment.save()
            message = new_message(AlertLevels.SUCCESS, "Votre demande de recrutement pour l'équipe " + futsal_team.acronym + " a bien été enregistrée. \
            Son gérant doit maintenant accepter ou refuser votre candidature. Vous serez informé de son choix dans votre boite à message.")
    else :
        message = new_message(AlertLevels.ERROR, "Votre demande de recrutement n'a pas aboutie ; aucun futsal_team_id fourni. Veuillez contacter le support.")
    return render(request, "futsal_teams.html", {'messages' : [message]})


@login_required
def futsal_team_enrollments(request):
    user = request.user
    person = mdl.person.search(user=user)
    futsal_team_enrollments = mdl.futsal_team_enrollment.search(person=person)
    return render(request, "futsal_team_enrollments.html", {'futsal_team_enrollments' : futsal_team_enrollments})


@login_required
def futsal_team_event(request, futsal_team_id, match_id):
    if futsal_team_id and match_id :
        futsal_team = mdl.futsal_team.search(id=futsal_team_id)[0]
        match = mdl.match.search(id=match_id)[0]
        match_participations = mdl.match_participation.search(match=match, futsal_team=futsal_team)
        persons=[mp.person for mp in match_participations]
        print('persons === ' + str(persons))
    return render(request, "match_participation.html", {'futsal_team' : futsal_team,
                                                         'match' : match,
                                                         'persons' : [mp.person for mp in match_participations],
                                                         'user_person' : mdl.person.search(user=request.user)[0],
                                                         'POSITIONS' : mdl.match_participation.MatchParticipation.POSITIONS})


def _save_participation(request, futsal_team_id, match_id):
    """
    Sauvegarde la aprticipation du user à un événement.
    Cette méthode est privée et séparée des "render" car elle est réutilisée à plusieurs endroits.
    """
    if futsal_team_id and match_id :
        futsal_team = mdl.futsal_team.search(id=futsal_team_id)[0]
        match = mdl.match.search(id=match_id)[0]
        user = request.user
        person = mdl.person.search(user=user)[0]
        match_participation = mdl.match_participation.MatchParticipation(futsal_team=futsal_team,
                                                                         match=match,
                                                                         person=person,
                                                                         position=request.POST['position'])
        match_participation.save()
        message = new_message(AlertLevels.SUCCESS, "Vous participez désormais à l'événement du " + str(match.date) + " de l'équipe " + futsal_team.acronym + ".")
    else :
        futsal_team = None
        matchs = None
        persons = None
        message = new_message(AlertLevels.ERROR, "Votre demande n'a pas aboutie. Aucun id fourni pour futsal_team. Veuillez contacter le support.")
    return {'futsal_team' : futsal_team,
            'account' : futsal_team.account,
            'messages' : [message]}


@login_required
def match_participation_save(request, futsal_team_id, match_id):
    infos = _save_participation(request, futsal_team_id, match_id)
    matchs = mdl.predicted_match.get_matchs(futsal_team=info['futsal_team'])
    futsal_team_enrollments = mdl.futsal_team_enrollment.search(futsal_team=info['futsal_team'])
    persons = [fte.person for fte in futsal_team_enrollments]
    infos['matchs'] = matchs
    infos['persons'] = persons
    return render(request, "futsal_team.html", infos)


@login_required
def match_participation_delete(request, futsal_team_id, match_id):
    if futsal_team_id and match_id :
        futsal_team = mdl.futsal_team.search(id=futsal_team_id)[0]
        match = mdl.match.search(id=match_id)[0]
        user = request.user
        person = mdl.person.search(user=user)[0]
        nb_rows_deleted = mdl.match_participation.delete(match, person, futsal_team)
        if nb_rows_deleted == 0 :
            message = new_message(AlertLevels.ERROR, "Une erreur s'est produite ; nous n'avons pas su vous désincrire de l'événement. Veuillez contacter le support.")
        else :
            message = new_message(AlertLevels.SUCCESS, "Vous ne faites désormais plus partie de l'événement du " + str(match.date) + " de l'équipe " + futsal_team.acronym + ".")
        matchs = mdl.match.search(futsal_team=futsal_team)
        futsal_team_enrollments = mdl.futsal_team_enrollment.search(futsal_team=futsal_team)
        persons = [fte.person for fte in futsal_team_enrollments]
    else :
        futsal_team = None
        matchs = None
        persons = None
        message = new_message(AlertLevels.ERROR, "Votre demande n'a pas aboutie. Aucun id fourni pour futsal_team. Veuillez contacter le support.")
    return render(request, "futsal_team.html", {'futsal_team' : futsal_team,
                                                'account' : futsal_team.account,
                                                'matchs' : matchs,
                                                'persons' : persons,
                                                'messages' : [message]})
@login_required
def matchs(request):
    form = MatchsForm()
    return render(request, "matchs.html")


@login_required
def matchs_search(request):
    if request.method == 'POST':
        form = MatchsForm(request.POST)
        if form.is_valid() :
            futsal_team_denomination = form.cleaned_data['futsal_team_denomination']
            sport_hall_denomination = form.cleaned_data['sport_hall_denomination']
            predicted_matchs = mdl.predicted_match.search(futsal_team_denomination=futsal_team_denomination, sport_hall_denomination=sport_hall_denomination)
            matchs = [pm.match for pm in predicted_matchs]
        else :
            matchs = None
    else :
        form = MatchsForm()
    return render(request, "matchs.html", {'form' : form,
                                           'matchs' : matchs})
