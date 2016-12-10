from django.conf.urls import url
from django.contrib import admin
from Management import views as Management_views

urlpatterns = [
	url(r'^login/$', Management_views.Login.as_view(), name='login'),
	
]
