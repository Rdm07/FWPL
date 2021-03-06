# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-10 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoalAndAssistAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_scorer', models.CharField(max_length=30)),
                ('assist_giver', models.CharField(max_length=30)),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoalAndAssistAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_scorer', models.CharField(max_length=30)),
                ('assist_giver', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GroupRanksAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_1', models.CharField(max_length=30)),
                ('rank_2', models.CharField(max_length=30)),
                ('rank_3', models.CharField(max_length=30)),
                ('rank_4', models.CharField(max_length=30)),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroupRanksAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_1', models.CharField(max_length=30)),
                ('rank_2', models.CharField(max_length=30)),
                ('rank_3', models.CharField(max_length=30)),
                ('rank_4', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LineupAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_1', models.CharField(max_length=30)),
                ('player_2', models.CharField(max_length=30)),
                ('player_3', models.CharField(max_length=30)),
                ('player_4', models.CharField(max_length=30)),
                ('player_5', models.CharField(max_length=30)),
                ('player_6', models.CharField(max_length=30)),
                ('player_7', models.CharField(max_length=30)),
                ('player_8', models.CharField(max_length=30)),
                ('player_9', models.CharField(max_length=30)),
                ('player_10', models.CharField(max_length=30)),
                ('player_11', models.CharField(max_length=30)),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='LineupAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_1', models.CharField(max_length=30)),
                ('player_2', models.CharField(max_length=30)),
                ('player_3', models.CharField(max_length=30)),
                ('player_4', models.CharField(max_length=30)),
                ('player_5', models.CharField(max_length=30)),
                ('player_6', models.CharField(max_length=30)),
                ('player_7', models.CharField(max_length=30)),
                ('player_8', models.CharField(max_length=30)),
                ('player_9', models.CharField(max_length=30)),
                ('player_10', models.CharField(max_length=30)),
                ('player_11', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Matchday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_number', models.IntegerField()),
                ('q_text', models.TextField()),
                ('margin', models.IntegerField(default=0)),
                ('bonus_allowed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScorelineAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_score', models.IntegerField()),
                ('away_team_score', models.IntegerField()),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ScorelineAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_score', models.IntegerField()),
                ('away_team_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SingleIntegerAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='SingleIntegerAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SinglePlayerTeamAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=30)),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='SinglePlayerTeamAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TeamAndValueAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamAndValueAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WinDrawLoseAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('Win', 'Win'), ('Draw', 'Draw'), ('Lose', 'Lose')], max_length=5)),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='WinDrawLoseAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('Win', 'Win'), ('Draw', 'Draw'), ('Lose', 'Lose')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='YesNoAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('bonus', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='YesNoAnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('for_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='YNAS', to='Management.Question')),
            ],
        ),
    ]
