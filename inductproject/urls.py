"""inductproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as ad_views
from snapp.forms import LoginForm
from rest_framework.urlpatterns import format_suffix_patterns
from snapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('snapp.urls')),
    url(r'^home/login/$', ad_views.login, {'template_name':'login.html', 'authentication_form': LoginForm},name= 'login'),
    url(r'^list/login/$', ad_views.login, {'template_name':'login.html', 'authentication_form': LoginForm},name= 'login'),
    url(r'^login/$', ad_views.login, {'template_name':'login.html', 'authentication_form': LoginForm},name= 'login'),
    url(r'^logout/$', ad_views.logout, {'next_page': '/login'}, name= 'logout'),
    url(r'^instancelist/$', views.SNInstanceConfiguredList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)