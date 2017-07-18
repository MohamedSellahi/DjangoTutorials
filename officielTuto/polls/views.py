from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# this is the page thay would be laoded automatically 
# if we request /polls/
def index(request):
  return HttpResponse("Hello, world. You are the tyhe polls index.")


def login(request):
  return HttpResponse("this is the login page")