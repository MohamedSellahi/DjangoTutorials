# this is the URLs Router for the polls app 
"""
Remember : url(regex, view, kwargs=None, name=None)[source]


"""
from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^login', views.login, name="login"),
  url(r'^$', views.index, name='index'),
]
