from django import forms
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import ModelForm
from django.template.defaultfilters import filesizeformat

from material import *

from models import *

from Player.models import Profile

class LoginForm(forms.Form):
    """
    Common Login Form for all Users.
    """
    username = forms.CharField(required=True, label='Username', max_length=50)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, initial=False,
                                     label='Remember Me')


class ProfileForm(UserCreationForm):

	first_name = forms.CharField(max_length=200, required=True)
	last_name = forms.CharField(max_length=200, required=True)
	email = forms.EmailField(required=True)

	def save(self, commit=True):
		user = super(ProfileForm, self).save(commit=False)
		user.email = self.cleaned_data.get('email')
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		if commit:
			user.save()
		return user
	
	class Meta:
		model = Profile
		fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
