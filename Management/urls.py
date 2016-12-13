from django.conf.urls import url
from django.contrib import admin
from Management import views

urlpatterns = [
	url(r'^login/$', views.Login.as_view(), name='login'),
	url(r'^logout/$', views.Logout.as_view(), name='logout'),
	url(r'^register/$', views.Register.as_view(), name='register'),
	url(r'^home/$', views.Home.as_view(), name='home'),
	url(r'^register-confirm/$', views.RegisterConfirm.as_view(), name='register-confirm'),
]
