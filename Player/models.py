from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# from Performance.models import *

# Create your models here.

class Profile(models.Model):
	User = models.OneToOneField(User)
	First_Name = models.CharField(max_length = 50)
	Last_Name = models.CharField(max_length = 50)
	Email = models.EmailField(max_length=254)

	def __unicode__(self):
		return self.First_Name
