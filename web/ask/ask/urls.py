"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from qa import views

urlpatterns = [
<<<<<<< HEAD

#	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/', admin.site.urls),

	url(r'^$', views.test, name='index'),

#/
#	url(r'^$', 'qa.views.test', name='index'),
#/login/
	url(r'login/$', views.aaa, name='login'),
=======
#	url(r'^$', views.test, name='index'),
	url(r'^admin/', include(admin.site.urls)),


#/
	url(r'^$', 'qa.views.test', name='index'),
#/login/
	url(r'login/$', views.test, name='login'),
>>>>>>> 2ab6c2dc0cdfd91ada8694f15d5499163a52a21d
#/signup/
	url(r'signup/$', views.test, name='signup'),
#/ask/
	url(r'ask/$', views.test, name='ask'),
#/popular/
	url(r'popular/$', views.test, name='popular'),
#/new/
	url(r'new/$', views.test, name='new'),
#/question/<123>/    # вместо <123> - произвольный ID
	url(r'^question/(?P<id>[0-9]+)/$', views.aaa, name='question'),
	


]
