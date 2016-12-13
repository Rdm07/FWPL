from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from Player.models import *
from Seasons.models import *

# Create your models here.

class Matchday(models.Model):
	day = models.CharField(max_length = 2)
	deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
	season = models.ForeignKey(AllSeason, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.day

class Question(models.Model):
	q_number = models.CharField(max_length=2)
	q_text = models.TextField()
	limit_answer_types = models.Q(app_label = 'Management')
	answer_type = models.ForeignKey(ContentType, limit_choices_to = limit_answer_types, related_name='Answer_Type', on_delete=models.CASCADE)
	limit_answer_set_types = models.Q(app_label = 'Management')
	answer_set_type = models.ForeignKey(ContentType, limit_choices_to = limit_answer_set_types, related_name='Answer_Set_Type', on_delete=models.CASCADE)
	margin = models.IntegerField(default = 0)
	bonus_allowed = models.BooleanField(default = True)
	for_matchday = models.ForeignKey(Matchday, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_matchday.day)+'_'+self.q_number

class SinglePlayerTeamAnswer(models.Model):
	answer = models.CharField(max_length = 30)
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'SPTA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class YesNoAnswer(models.Model):
	answer = models.CharField(max_length = 30, choices = (('Yes','Yes'), ('No','No'), ))
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'YNA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class WinDrawLoseAnswer(models.Model):
	answer = models.CharField(max_length = 30, choices = (('Win','Win'), ('Draw','Draw'), ('Lose','Lose'),))
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'WDLA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class ScorelineAnswer(models.Model):
	home_team_score = models.IntegerField()
	away_team_score = models.IntegerField()
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'SA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class SingleIntegerAnswer(models.Model):
	answer = models.IntegerField()
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'SIA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class LineupAnswer(models.Model):
	player_1 = models.CharField(max_length = 30)
	player_2 = models.CharField(max_length = 30)
	player_3 = models.CharField(max_length = 30)
	player_4 = models.CharField(max_length = 30)
	player_5 = models.CharField(max_length = 30)
	player_6 = models.CharField(max_length = 30)
	player_7 = models.CharField(max_length = 30)
	player_8 = models.CharField(max_length = 30)
	player_9 = models.CharField(max_length = 30)
	player_10 = models.CharField(max_length = 30)
	player_11 = models.CharField(max_length = 30)
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'LA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class GroupRanksAnswer(models.Model):
	rank_1 = models.CharField(max_length = 30)
	rank_2 = models.CharField(max_length = 30)
	rank_3 = models.CharField(max_length = 30)
	rank_4 = models.CharField(max_length = 30)
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'GRA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class TeamAndValueAnswer(models.Model):
	team = models.CharField(max_length = 30)
	value = models.IntegerField()
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'TAVA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class GoalAndAssistAnswer(models.Model):
	goal_scorer = models.CharField(max_length = 30)
	assist_giver = models.CharField(max_length = 30)
	bonus = models.BooleanField(default = False)
	for_question = models.ForeignKey(Question, related_name = 'GAAA', on_delete=models.CASCADE)
	by_player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.by_player.first_name)

class SinglePlayerTeamAnswerSet(models.Model):
	answer = models.CharField(max_length = 30)
	for_question = models.ForeignKey(Question, related_name = 'SPTAS', on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)

class YesNoAnswerSet(models.Model):
	answer = models.CharField(max_length = 30, choices = (('Yes','Yes'), ('No','No'), ))
	for_question = models.ForeignKey(Question, related_name = 'YNAS', on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)

class WinDrawLoseAnswerSet(models.Model):
	answer = models.CharField(max_length = 30, choices = (('Win','Win'), ('Draw','Draw'), ('Lose','Lose'),))
	for_question = models.ForeignKey(Question, related_name = 'WDLAS', on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)

class ScorelineAnswerSet(models.Model):
	home_team_Score = models.IntegerField()
	away_team_Score = models.IntegerField()
	for_question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)

class SingleIntegerAnswerSet(models.Model):
	answer = models.IntegerField()
	for_question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)

class LineupAnswerSet(models.Model):
	player_1 = models.CharField(max_length = 30)
	player_2 = models.CharField(max_length = 30)
	player_3 = models.CharField(max_length = 30)
	player_4 = models.CharField(max_length = 30)
	player_5 = models.CharField(max_length = 30)
	player_6 = models.CharField(max_length = 30)
	player_7 = models.CharField(max_length = 30)
	player_8 = models.CharField(max_length = 30)
	player_9 = models.CharField(max_length = 30)
	player_10 = models.CharField(max_length = 30)
	player_11 = models.CharField(max_length = 30)
	for_question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)

class GroupRanksAnswerSet(models.Model):
	rank_1 = models.CharField(max_length = 30)
	rank_2 = models.CharField(max_length = 30)
	rank_3 = models.CharField(max_length = 30)
	rank_4 = models.CharField(max_length = 30)
	for_question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)

class TeamAndValueAnswerSet(models.Model):
	team = models.CharField(max_length = 30)
	value = models.IntegerField()
	for_question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)

class GoalAndAssistAnswerSet(models.Model):
	goal_scorer = models.CharField(max_length = 30)
	assist_giver = models.CharField(max_length = 30)
	for_question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.for_question.for_matchday.day)+'_'+str(self.for_question.q_number)
