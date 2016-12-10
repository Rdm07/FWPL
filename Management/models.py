from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from Player.models import Profile
from Seasons.models import AllSeason

# Create your models here.

class Matchday(models.Model):
	MatchDay = models.CharField(max_length = 2)
	Deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
	Season = models.ForeignKey(AllSeason, on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday'+self.MatchDay

class Question(models.Model):
	Question_Number = models.CharField(max_length=2)
	Question = models.TextField()
	Limit_Answer_Types = models.Q(app_label = 'Management')
	Answer_Type = models.ForeignKey(ContentType, limit_choices_to = Limit_Answer_Types, related_name='Answer_Type', on_delete=models.CASCADE)
	Limit_Answer_Set_Types = models.Q(app_label = 'Management')
	Answer_Set_Type = models.ForeignKey(ContentType, limit_choices_to = Limit_Answer_Set_Types, related_name='Answer_Set_Type', on_delete=models.CASCADE)
	Margin = models.IntegerField(default = 0)
	Bonus_Allowed = models.BooleanField(default = True)
	For_Matchday = models.ForeignKey(Matchday, on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Matchday.MatchDay)+'_Question_'+self.Question_Number

class SinglePlayerTeamAnswer(models.Model):
	Answer = models.CharField(max_length = 30)
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'SPTA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class YesNoAnswer(models.Model):
	Answer = models.CharField(max_length = 30, choices = (('Yes','Yes'), ('No','No'), ))
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'YNA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class WinDrawLoseAnswer(models.Model):
	Answer = models.CharField(max_length = 30, choices = (('Win','Win'), ('Draw','Draw'), ('Lose','Lose'),))
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'WDLA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class ScorelineAnswer(models.Model):
	Home_Team_Score = models.IntegerField()
	Away_Team_Score = models.IntegerField()
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'SA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class SingleIntegerAnswer(models.Model):
	Answer = models.IntegerField()
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'SIA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class LineupAnswer(models.Model):
	Player_1 = models.CharField(max_length = 30)
	Player_2 = models.CharField(max_length = 30)
	Player_3 = models.CharField(max_length = 30)
	Player_4 = models.CharField(max_length = 30)
	Player_5 = models.CharField(max_length = 30)
	Player_6 = models.CharField(max_length = 30)
	Player_7 = models.CharField(max_length = 30)
	Player_8 = models.CharField(max_length = 30)
	Player_9 = models.CharField(max_length = 30)
	Player_10 = models.CharField(max_length = 30)
	Player_11 = models.CharField(max_length = 30)
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'LA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class GroupRanksAnswer(models.Model):
	Rank_1 = models.CharField(max_length = 30)
	Rank_2 = models.CharField(max_length = 30)
	Rank_3 = models.CharField(max_length = 30)
	Rank_4 = models.CharField(max_length = 30)
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'GRA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class TeamAndValueAnswer(models.Model):
	Team = models.CharField(max_length = 30)
	Value = models.IntegerField()
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'TAVA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class GoalAndAssistAnswer(models.Model):
	Goal_Scorer = models.CharField(max_length = 30)
	Assist_Giver = models.CharField(max_length = 30)
	Bonus = models.BooleanField(default = False)
	For_Question = models.ForeignKey(Question, related_name = 'GAAA', on_delete=models.CASCADE)
	By_Player = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.By_Player.First_Name)

class SinglePlayerTeamAnswerSet(models.Model):
	Answer = models.CharField(max_length = 30)
	For_Question = models.ForeignKey(Question, related_name = 'SPTAS', on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)

class YesNoAnswerSet(models.Model):
	Answer = models.CharField(max_length = 30, choices = (('Yes','Yes'), ('No','No'), ))
	For_Question = models.ForeignKey(Question, related_name = 'YNAS', on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)

class WinDrawLoseAnswerSet(models.Model):
	Answer = models.CharField(max_length = 30, choices = (('Win','Win'), ('Draw','Draw'), ('Lose','Lose'),))
	For_Question = models.ForeignKey(Question, related_name = 'WDLAS', on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)

class ScorelineAnswerSet(models.Model):
	Home_Team_Score = models.IntegerField()
	Away_Team_Score = models.IntegerField()
	For_Question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)

class SingleIntegerAnswerSet(models.Model):
	Answer = models.IntegerField()
	For_Question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)

class LineupAnswerSet(models.Model):
	Player_1 = models.CharField(max_length = 30)
	Player_2 = models.CharField(max_length = 30)
	Player_3 = models.CharField(max_length = 30)
	Player_4 = models.CharField(max_length = 30)
	Player_5 = models.CharField(max_length = 30)
	Player_6 = models.CharField(max_length = 30)
	Player_7 = models.CharField(max_length = 30)
	Player_8 = models.CharField(max_length = 30)
	Player_9 = models.CharField(max_length = 30)
	Player_10 = models.CharField(max_length = 30)
	Player_11 = models.CharField(max_length = 30)
	For_Question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)

class GroupRanksAnswerSet(models.Model):
	Rank_1 = models.CharField(max_length = 30)
	Rank_2 = models.CharField(max_length = 30)
	Rank_3 = models.CharField(max_length = 30)
	Rank_4 = models.CharField(max_length = 30)
	For_Question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)

class TeamAndValueAnswerSet(models.Model):
	Team = models.CharField(max_length = 30)
	Value = models.IntegerField()
	For_Question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)

class GoalAndAssistAnswerSet(models.Model):
	Goal_Scorer = models.CharField(max_length = 30)
	Assist_Giver = models.CharField(max_length = 30)
	For_Question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __unicode__(self):
		return 'Matchday_'+str(self.For_Question.For_Matchday.MatchDay)+'_Question_'+str(self.For_Question.Question_Number)
