from base.models import *
from django.contrib import admin

admin.site.register(account_transaction.AccountTransaction,
                    account_transaction.AccountTransactionAdmin)

admin.site.register(account.Account,
                    account.AccountAdmin)

admin.site.register(futsal_team.FutsalTeam,
                    futsal_team.FutsalTeamAdmin)

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

admin.site.register(person_address.PersonAddress,
                    person_address.PersonAddressAdmin)

admin.site.register(sport_hall.SportHall,
                    sport_hall.SportHallAdmin)

admin.site.register(sport_hall_address.SportHallAddress,
                    sport_hall_address.SportHallAddressAdmin)

admin.site.register(transaction.Transaction,
                    transaction.TransactionAdmin)
