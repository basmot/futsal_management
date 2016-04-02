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

from base.models import *
from django.contrib import admin

admin.site.register(account_transaction.AccountTransaction,
                    account_transaction.AccountTransactionAdmin)

admin.site.register(account.Account,
                    account.AccountAdmin)

admin.site.register(futsal_team.FutsalTeam,
                    futsal_team.FutsalTeamAdmin)

admin.site.register(futsal_team_enrollment.FutsalTeamEnrollment,
                    futsal_team_enrollment.FutsalTeamEnrollmentAdmin)

admin.site.register(inscription_state.InscriptionState,
                    inscription_state.InscriptionStateAdmin)

admin.site.register(league_enrollment.LeagueEnrollment,
                    league_enrollment.LeagueEnrollmentAdmin)

admin.site.register(league.League,
                    league.LeagueAdmin)

admin.site.register(match_participation.MatchParticipation,
                    match_participation.MatchParticipationAdmin)

admin.site.register(match.Match,
                    match.MatchAdmin)

admin.site.register(person.Person,
                    person.PersonAdmin)

admin.site.register(predicted_match.PredictedMatch,
                    predicted_match.PredictedMatchAdmin)

admin.site.register(person_address.PersonAddress,
                    person_address.PersonAddressAdmin)

admin.site.register(sport_hall.SportHall,
                    sport_hall.SportHallAdmin)

admin.site.register(sport_hall_address.SportHallAddress,
                    sport_hall_address.SportHallAddressAdmin)

admin.site.register(transaction.Transaction,
                    transaction.TransactionAdmin)
