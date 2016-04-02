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

"""futsal_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout

from base.views import common, futsal_team, futsal_team_enrollment, match

urlpatterns = [
    url(r'^$', common.home, name='home'),

    url(r'^admin/', admin.site.urls),

    url(r'^login/$', common.login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^futsal_team_enrollments/$', futsal_team_enrollment.futsal_team_enrollments, name='futsal_team_enrollments'),

    url(r'^futsal_teams/$', futsal_team.futsal_teams, name='futsal_teams'),
    url(r'^futsal_teams/search$', futsal_team.futsal_teams_search, name='futsal_teams_search'),
    url(r'^futsal_teams/([0-9]+)$', futsal_team.futsal_team, name='futsal_team'),
    url(r'^futsal_teams/([0-9]+)/enrollment$', futsal_team.futsal_team_enrollment, name='futsal_team_enrollment'),
    url(r'^futsal_teams/([0-9]+)/matchs/([0-9]+)$', futsal_team.futsal_team_event, name='futsal_team_event'),
    url(r'^futsal_teams/([0-9]+)/matchs/([0-9]+)/participate$', futsal_team.match_participation_save, name='match_participation_save'),
    url(r'^futsal_teams/([0-9]+)/matchs/([0-9]+)/delete_participation$', futsal_team.match_participation_delete, name='match_participation_delete'),

    url(r'^matchs/$', match.matchs, name='matchs'),
    url(r'^matchs/search$', match.matchs_search, name='matchs_search'),

    url(r'^user_enrollment/$', common.user_enrollment, name='user_enrollment'),
]
