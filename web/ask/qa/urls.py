from django.conf.urls import url

from . import views

urlpatterns = [
#    url(r'^$', views.index, name='index'),

#/
	url(r'^$', views.aaa, name='indexName_IN_urls.py'),
#/login/
#	url(r'login/^$', views.test, name='login'),
#/signup/
#	url(r'signup/^$', views.test, name='signup'),
#/ask/
#	url(r'ask/^$', views.test, name='ask'),
#/popular/
#	url(r'popular/^$', views.test, name='popular'),
#/new/
#	url(r'new/^$', views.test, name='new'),
#/question/<123>/    # вместо <123> - произвольный ID
#	url(r'^question/(?P<id>[0-9]+)/^$', views.test, name='question'),
	

]