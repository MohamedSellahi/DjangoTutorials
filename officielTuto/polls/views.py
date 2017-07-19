from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# this is the page thay would be laoded automatically 
# if we request /polls/
def index(request):
  return HttpResponse("Hello, world. You are the tyhe polls index.")


def login(request):
  return HttpResponse("this is the login page")

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the resutls of question %s."
  return HttpResponse(response % question_id)

def vote(request,question_id):
  return HttpResponse("You are voting on question %s. "%question_id)
