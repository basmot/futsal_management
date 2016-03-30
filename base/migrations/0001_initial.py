# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-30 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Account')),
            ],
        ),
        migrations.CreateModel(
            name='FutsalTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=10)),
                ('denomination', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Account')),
            ],
        ),
        migrations.CreateModel(
            name='FutsalTeamEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_enrollment', models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REFUSED', 'Refused')], default='PENDING', max_length=30)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_enrollment', models.DateTimeField(default=django.utils.timezone.now)),
                ('futsal_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.FutsalTeam')),
            ],
        ),
        migrations.CreateModel(
            name='InscriptionState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REFUSED', 'Refused')], default='PENDING', max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=10)),
                ('denomination', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(blank=True, choices=[('D1', 'Division 1 (National)'), ('D2', 'Division 2 (National)'), ('D3', 'Division 3 (National)'), ('P1', 'Provincial 1'), ('P2', 'Provincial 2'), ('P3', 'Provincial 3'), ('P4', 'Provincial 4'), ('P5', 'Provincial 5')], max_length=2, null=True)),
                ('category', models.CharField(blank=True, choices=[('J', 'Junior'), ('S', 'Senior'), ('V', 'Veteran'), ('F', 'Woman')], max_length=1, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('futsal_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.FutsalTeam')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('match_type', models.CharField(choices=[('FRIENDLY', 'Friendly'), ('TRAINING', 'Training'), ('OFFICIAL', 'Official')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MatchParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('co', 'Coach'), ('ca', 'Captain'), ('d', 'Deleguee'), ('k', 'Keeper'), ('p', 'Player'), ('r', 'Referee')], max_length=2)),
                ('futsal_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.FutsalTeam')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unknown')], default='U', max_length=1, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_mobile', models.CharField(blank=True, max_length=30, null=True)),
                ('language', models.CharField(choices=[('fr', 'French'), ('en', 'English')], default='fr', max_length=30, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Person')),
            ],
        ),
        migrations.CreateModel(
            name='SportHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=10)),
                ('denomination', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SportHallAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('sport_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.SportHall')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('note', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='sporthall',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.SportHallAddress'),
        ),
        migrations.AddField(
            model_name='matchparticipation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Person'),
        ),
        migrations.AddField(
            model_name='match',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.SportHall'),
        ),
        migrations.AddField(
            model_name='leagueenrollment',
            name='home_sport_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.SportHall'),
        ),
        migrations.AddField(
            model_name='leagueenrollment',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.League'),
        ),
        migrations.AddField(
            model_name='futsalteamenrollment',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Person'),
        ),
        migrations.AddField(
            model_name='accounttransaction',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Transaction'),
        ),
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Person'),
        ),
    ]
