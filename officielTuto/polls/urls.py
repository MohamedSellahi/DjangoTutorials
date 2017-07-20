# this is the URLs Router for the polls app 
"""
Remember : url(regex, view, kwargs=None, name=None)[source]


"""
from django.conf.urls import url
from . import views

# Namespace this urls 

app_name = 'polls'

urlpatterns = [
  # url(r'^login', views.login, name="login"),
  #ex /polls/
  url(r'^$', views.index, name='index'),
  
  # ex /polls/5/
  url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),

  #ex /polls/5/details
  url(r'^(?P<question_id>[0-9]+)/details/$', views.detail2, name="details"),

  # ex /polls/5/results/
  url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),

  # ex /polls/5/vote/
  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
  
  # any other thing 
  url(r'^.?', views.index, name='index'),
]
