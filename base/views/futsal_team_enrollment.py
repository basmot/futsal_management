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
def futsal_team_enrollments(request):
    user = request.user
    person = mdl.person.search(user=user)
    futsal_team_enrollments = mdl.futsal_team_enrollment.search(person=person)
    return render(request, "futsal_team_enrollments.html", {'futsal_team_enrollments' : futsal_team_enrollments})
