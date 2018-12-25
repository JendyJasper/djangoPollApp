from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# from django.template import loader, RequestContext
# Create your views here.

def index(request):
	latest_questions = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {'latest_questions': latest_questions}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = Question.objects.get(pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	return HttpResponse("These are the results view of the question: {}".format(question_id))

def vote(request, question_id):
	return HttpResponse("Vote on question: {}".format(question_id))