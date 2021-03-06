from django.shortcuts import render
from polls.models import Choice,Question
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]

    context = {'latest_question_list' : latest_question_list}

    return render(request, 'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    pass

def results(request, question_id):
    pass