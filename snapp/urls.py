from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.logi, name='home'),
    url(r'^list/$', views.listall, name='list'),
    url(r'^incident_details/(?P<sys_id>[A-Za-z0-9_@./&+-]+)$', views.incidentdet, name='incident_details'),
    url(r'^create/$', views.createinc, name='createinc'),
    url(r'^createdinc/$', views.createdinc, name='createdinc'),
    #url(r'^createdinc/$', views.createdinc, name='creationinc'),
]