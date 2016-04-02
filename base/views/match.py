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

from base.forms import MatchsForm
from base import models as mdl
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.views.reference import AlertLevels, new_message


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
