print '-----> apps/signals.py'

import poplib

from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from django.utils.encoding import smart_str
from itertools import chain

from django.db.models.signals import post_save
from django.dispatch import receiver

from Management.models import *

@receiver(post_save, sender=SinglePlayerTeamAnswerSet, dispatch_uid="SPTA Points")
def allocate_points_SPTA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = SinglePlayerTeamAnswer.objects.filter(for_question=question)
	for a in answer_list:
		if a.points == 0:
			if a.answer == instance.answer:
				if a.bonus == True:
					a.points = 2
					a.save()
				else:
					a.points = 1
					a.save()
			else:
				if a.bonus == True:
					a.points = -2
					a.save()
				else:
					a.points = 0
					a.save()


@receiver(post_save, sender=YesNoAnswerSet, dispatch_uid="YNA Points")
def allocate_points_YNA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = YesNoAnswer.objects.filter(for_question=question)
	for a in answer_list:
		if a.points == 0:
			if a.answer == instance.answer:
				if a.bonus == True:
					a.points = 2
					a.save()
				else:
					a.points = 1
					a.save()
			else:
				if a.bonus == True:
					a.points = -2
					a.save()
				else:
					a.points = 0
					a.save()
			
@receiver(post_save, sender=WinDrawLoseAnswerSet, dispatch_uid="WDLA Points")
def allocate_points_WDLA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = WinDrawLoseAnswer.objects.filter(for_question=question)
	for a in answer_list:
		if a.points == 0:
			if a.answer == instance.answer:
				if a.bonus == True:
					a.points = 2
					a.save()
				else:
					a.points = 1
					a.save()
			else:
				if a.bonus == True:
					a.points = -2
					a.save()
				else:
					a.points = 0
					a.save()

@receiver(post_save, sender=ScorelineAnswerSet, dispatch_uid="SA Points")
def allocate_points_SA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = ScorelineAnswer.objects.filter(for_question=question)
	for a in answer_list:
		if a.points == 0:
			if (a.home_team_score == instance.home_team_score and a.away_team_score == instance.away_team_score):
				if a.bonus == True:
					a.points = 2
					a.save()
				else:
					a.points = 1
					a.save()
			else:
				if a.bonus == True:
					a.points = -2
					a.save()
				else:
					a.points = 0
					a.save()

@receiver(post_save, sender=SingleIntegerAnswerSet, dispatch_uid="SIA Points")
def allocate_point_SIA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = SingleIntegerAnswer.objects.filter(for_question=question)
	margin = question.margin
	for a in answer_list:
		if a.points == 0:
			if ((instance.answer - margin) <= a.answer <= (instance.answer + margin)):
				if a.bonus == True:
					a.points = 2
				else:
					a.points = 1
				a.save()
			else:
				if a.bonus == True:
					a.points = -2
				else:
					a.points = 0
				a.save()

@receiver(post_save, sender=LineupAnswerSet, dispatch_uid="LA Points")
def allocate_points_LA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = LineupAnswer.objects.filter(for_question=question)
	margin = question.margin
	p_list_aset = sorted[instance.player_1, instance.player_2, instance.player_3, instance.player_4, instance.player_5, instance.player_6, instance.player_7, instance.player_8, instance.player_9, instance.player_10, instance.player_11]
	for a in answer_list:
		p_list_a = sorted[a.player_1, a.player_2, a.player_3, a.player_4, a.player_5, a.player_6, a.player_7, a.player_8, a.player_9, a.player_10, a.player_11]
		count = 0
		for x in range(0,10):
			if p_list_a[x] == p_list_aset[x]:
				count = count + 1

		if a.points == 0:
			if ((a.team == instance.team) and ((11-margin) <= count <= 11)):
				if a.bonus == True:
					a.points = 2
				else:
					a.points = 1
				a.save()
			else:
				if a.bonus == True:
					a.points = -2
				else:
					a.points = 0
				a.save()

@receiver(post_save, sender=GroupRanksAnswerSet, dispatch_uid="GRA Points")
def allocate_points_GRA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = GroupRanksAnswer.objects.filter(for_question=question)
	for a in answer_list:
		if a.points == 0:
			if (a.rank_1 == instance.rank_1 and a.rank_2 == instance.rank_2 and
				a.rank_3 == instance.rank_3 and a.rank_4 == instance.rank_4):
				if a.bonus == True:
					a.points = 2
				else:
					a.points = 1
				a.save()
			else:
				if a.bonus == True:
					a.points = -2
				else:
					a.points = 0
				a.save()

@receiver(post_save, sender=TeamAndValueAnswerSet, dispatch_uid="TAVA Points")
def allocate_points_TAVA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = TeamAndValueAnswer.objects.filter(for_question=question)
	margin = question.margin
	for a in answer_list:
		if a.points == 0:
			if (a.team == instance.team and (instance.value - margin) <= a.value <= (instance.value + margin)):
				if a.bonus == True:
					a.points = 2
				else:
					a.points = 1
				a.save()
			else:
				if a.bonus == True:
					a.points = -2
				else:
					a.points = 0
				a.save()

@receiver(post_save, sender=GoalAndAssistAnswerSet, dispatch_uid="GAAA Points")
def allocate_points_GAAA(sender, **kwargs):
	instance = kwargs['instance']
	question = instance.for_question
	answer_list = GoalAndAssistAnswer.objects.filter(for_question=question)
	for a in answer_list:
		if a.points == 0:
			if (a.goal_scorer == instance.goal_scorer and a.assist_giver == instance.away_team_score):
				if a.bonus == True:
					a.points = 2
				else:
					a.points = 1
				a.save()
			else:
				if a.bonus == True:
					a.points = -2
				else:
					a.points = 0
				a.save()