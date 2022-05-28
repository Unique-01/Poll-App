from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django .views import generic
from .models import *

# Create your views here.\

class QuestionList(generic.ListView):
    queryset = Question.objects.all()
    template_name = 'index.html'

class QuestionDetail(generic.DetailView):
    model = Question
    template_name = 'question_detail.html'

class Result(generic.DetailView):
    model = Question
    template_name = 'results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

