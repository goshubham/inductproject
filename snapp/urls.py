from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.logi, name='home'),
    url(r'^list/$', views.listall, name='listv'),
]