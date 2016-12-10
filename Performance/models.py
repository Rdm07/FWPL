from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from Management.models import *

# Create your models here.

'''
Define Scoring Algorithms
'''

'''
Use in View
'''

'''
def SPTA_Score(Value1, Value2):
	if Value1 = Value2:
		return 1

	else:
		return 0

def YNA_Score(Value1, Value2):
	if Value1 = Value2:
		return 1

	else:
		return 0

def WDLA_Score(Value1, Value2):
	if Value1 = Value2:
		return 1

	else:
		return 0

def SA_Score(Value1, Value2, Value3, Value4):
	if Value1 = Value2:
		return 1

	else:
		return 0

def SIA_Score(Value1, Value2):
	if Value1 = Value2:
		return 1

	else:
		return 0

def LA_Score(Value1, Value2):
	Value1.sort()
	Value2.sort()
	Count = 0
	for x in range(0:10):
		if Value1[x] = Value2[x]:
			Count = Count+1

	return Count

def GRA_Score(Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8):
	if Value1 = Value5 and Value2 = Value6 and Value3 = Value7 and Value4 = Value8:
		return 1

	else:
		return 0

def TAVA_Score(Value1, Value2, Value3, Value4):
	if Value1 = Value3 and Value2 = Value4:
		return 1

	else:
		return 0

def GAAA_Score(Value1, Value2, Value3, Value4):
	if Value1 = Value3 and Value2 = Value4:
		return 1

	else:
		return 0

'''

class MatchdayPoint(models.Model):
	Matchday = models.ForeignKey(Matchday, on_delete = models.CASCADE)
	Player = models.ForeignKey(Profile, on_delete = models.CASCADE)
	Question_1 = models.IntegerField(editable = False)
	Question_2 = models.IntegerField(editable = False)
	Question_3 = models.IntegerField(editable = False)
	Question_4 = models.IntegerField(editable = False)
	Question_5 = models.IntegerField(editable = False)
	Question_6 = models.IntegerField(editable = False)
	Question_7 = models.IntegerField(editable = False)
	Question_8 = models.IntegerField(editable = False)
	Question_9 = models.IntegerField(editable = False)
	Question_10 = models.IntegerField(editable = False)

	def __unicode__(self):
		return str(self.Player.First_Name)+'_Matchday_'+str(self.Matchday.MatchDay)




	# Question 1

	# Q = Question.objects.filter(For_Matchday = Matchday)
	# N = Q.count()

	# Q_id = [[0] for i in range(N)]
	# Q_AT = [[0] for i in range(N)]
	# Q_AST = [[0] for i in range(N)]

	# for x in range(N):
	# 	Q_id[x] = Q.filter(Question_Number = x+1)[0].id
	# 	Q_AT[x] = Q.filter(Question_Number = x+1)[0].Answer_Type
	# 	Q_AST[x] = Q.filter(Question_Number = x+1)[0].Answer_Set_Type

	# for x in range(N):



	

	# for obj in Q1:
	# 	Q1_id = obj.id
	# 	Q1_AT_id = obj.Answer_Type.id
	# 	Q1_AST = obj.Answer_Set_Type

	# Q1_AT = ContentType.objects.get(model = str(Q1_AT_name))
	# A1 = Q1_AT.objects.filter(For_Question.id = Q1_id, By_Player = Player_id)
	# for obj in A1:
	# 	A1_Answer = obj.Answer

