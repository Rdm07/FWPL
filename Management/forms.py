from django import forms
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ModelForm
from django.template.defaultfilters import filesizeformat

from material import *

from models import *

class LoginForm(forms.Form):
    """
    Common Login Form for all Users.
    """
    username = forms.CharField(required=True, label='Username', max_length=50)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, initial=False,
                                     label='Remember Me')

