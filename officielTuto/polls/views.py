from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# from django.template import loader
from .models import Question, Choice
# Create your views here.

# this is the page thay would be laoded automatically 
# if we request /polls/

# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('polls/index.html')
#   context = {'latest_question_list':latest_question_list} # this is the variable to  be passet to the view
#   return HttpResponse(template.render(context, request))

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:3]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)


def login(request):
  return HttpResponse("this is the login page")

def detail(request, question_id):
  try:
    question = Question.objects.get(pk = question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', {'question': question})


def detail2(request, question_id):
  question = get_object_or_404(Question, pk = question_id)
  return render(request, 'polls/detail.html',{'question': question})

def results(request, question_id):
  question = get_object_or_404(Question, pk = question_id)
  return render(request, 'polls/results.html', {'question': question})
  
# you might think of race condition 
def vote(request,question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
            'question': question,
            'error_message':"You didn't select a choice"})
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing with data 
    # with post data. this prevents data from being 
    # posted twice is a user hits the back button
    # reverse will construct an url from route name and arguments 
  return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



# USING GENERIC VIEWS 

from django.views import generic

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """ Return the last five published questions """
    return Question.objects.order_by('-pub_date')[:5]


class DetailedView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultsView(generic.DeleteView):
  model = Question
  template_name = 'polls/results.html'
  context_object_name = 'question'


# vote view does not change 
