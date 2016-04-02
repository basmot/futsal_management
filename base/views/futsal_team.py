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

from base.forms import UserEnrollmentForm, FutsalTeamForm, MatchsForm
from base import models as mdl
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
def futsal_team_event(request, futsal_team_id, match_id):
    if futsal_team_id and match_id :
        futsal_team = mdl.futsal_team.search(id=futsal_team_id)[0]
        match = mdl.match.search(id=match_id)[0]
        match_participations = mdl.match_participation.search(match=match, futsal_team=futsal_team)
        persons=[mp.person for mp in match_participations]
    return render(request, "match_participation.html", {'futsal_team' : futsal_team,
                                                         'match' : match,
                                                         'persons' : [mp.person for mp in match_participations],
                                                         'user_person' : mdl.person.search(user=request.user)[0],
                                                         'POSITIONS' : mdl.match_participation.MatchParticipation.POSITIONS})


def _save_participation(request, futsal_team_id, match_id):
    """
    Sauvegarde la aprticipation du user à un événement.
    Cette méthode est privée et séparée des "render" car elle sera peut-être réutilisée à plusieurs endroits.
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
