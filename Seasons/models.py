from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AllSeason(models.Model):
	Name = models.CharField(max_length = 30)
	team = 'Team'
	indi = 'Indi'
	participation_choices = ((team, 'Team'), (indi, 'Individual'),)
	Participation = models.CharField(max_length=4, choices=participation_choices, default = indi,)
	Current = models.BooleanField(default=True)

	def __unicode__(self):
		return self.Name

# class PreviousSeasonDetail(models.Model):
# 	Name = models.CharField(max_length = 30)
# 	team = 'Team'
# 	indi = 'Indi'
# 	participation_choices = ((team, 'Team'), (indi, 'Individual'),)
# 	Participation = models.CharField(max_length=4, choices=participation_choices, default = indi,)
# 	Current = models.BooleanField(default=True)

# 	def __unicode__(self):
# 		return self.name

# class Team(models.Model):
# 	Name = models.CharField(max_length = 30)
# 	team = 'Team'
# 	indi = 'Indi'
# 	participation_choices = ((team, 'Team'), (indi, 'Individual'),)
# 	Participation = models.CharField(max_length=4, choices=participation_choices, default = indi,)
# 	Current = models.BooleanField(default=True)

# 	def __unicode__(self):
# 		return self.name

# class Team-Season-Relation(models.Model):
# 	Name = models.CharField(max_length = 30)
# 	team = 'Team'
# 	indi = 'Indi'
# 	participation_choices = ((team, 'Team'), (indi, 'Individual'),)
# 	Participation = models.CharField(max_length=4, choices=participation_choices, default = indi,)
# 	Current = models.BooleanField(default=True)

# 	def __unicode__(self):
# 		return self.name

# class Player-Season-Relation(models.Model):
# 	Name = models.CharField(max_length = 30)
# 	team = 'Team'
# 	indi = 'Indi'
# 	participation_choices = ((team, 'Team'), (indi, 'Individual'),)
# 	Participation = models.CharField(max_length=4, choices=participation_choices, default = indi,)
# 	Current = models.BooleanField(default=True)

# 	def __unicode__(self):
# 		return self.name
