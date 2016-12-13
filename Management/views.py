from django.shortcuts import render
import poplib

from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.forms import FileInput
from django.forms.models import modelform_factory
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.utils import timezone
from django.utils.encoding import smart_str
from django.views.generic import (View, ListView, TemplateView, DetailView, CreateView, UpdateView)

from Management import forms
from Management.forms import *
from Player.models import Profile

def handler400(request):
	return render(request, '400.html')


def handler403(request):
	return render(request, '403.html')


def handler404(request):
	return render(request, '404.html')


def handler500(request):
	return render(request, '500.html')


def handler503(request):
	return render(request, '503.html')


class Login(View):
	template_name = 'Management/login.html'

	def get(self, request):
		if request.user.is_authenticated():
			return redirect('home')
		form_my = LoginForm()
		return render(request, self.template_name, dict(form=form_my))

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect("home")
			else:
				return render(request, self.template_name, dict(form=form))
		else:
			return render(request, self.template_name, dict(form=form))

class Logout(View):
	def get(self, request):
		auth.logout(request)
		return redirect('login')

class Home(TemplateView):
	template_name = 'Management/home.html'

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['user'] = Profile.objects.get(username=self.request.user.username)
		return context

class Register(View):
	template_name = 'Management/register.html'

	def get(self, request):
		form_my = ProfileForm()
		return render(request, self.template_name, dict(form=form_my))

	def post(self, request):
		form = ProfileForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('register-confirm')
		else:
			return render(request, self.template_name, dict(form=form))

class RegisterConfirm(TemplateView):
	template_name = 'Management/register_confirm.html'

# class Questions(View):
# 	template_name = 'Management/questions.html'

# 	m = Matchday.objects.filter(day = 1)

# 	q = Question.objects.filter(for_matchday = m)

	# def get(self, request):
	# 	qnumber = q.q_number
	# 	qtext = q.q_text