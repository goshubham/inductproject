from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.logi, name='home'),
    url(r'^home/$', views.logi, name='homepage'),
    url(r'^list/$', views.listall, name='list'),
    url(r'^incident_details/(?P<sys_id>[A-Za-z0-9_@./&+-]+)$', views.incidentdet, name='incident_details'),
    url(r'^create/$', views.createinc, name='createinc'),
    url(r'^createdinc/$', views.createdinc, name='createdinc'),
    url(r'^update/$', views.updateinc, name='updateinc'),
    url(r'^update_select/(?P<number>[A-Za-z0-9_@./&+-]+)$', views.update_select, name='update_select'),
    url(r'^getUpdateDetail/$', views.getUpdateDetail, name='getUpdateDetail'),

    url(r'^delete/$', views.deleteinc, name='deleteinc'),
    url(r'^delete_select/$', views.delete_select, name='delete_select'),
]