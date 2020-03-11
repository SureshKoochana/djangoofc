from .models import Question

from django.http import Http404
from django.shortcuts import get_object_or_404,render


# Create your views here.

def index(request):
    #A shortcut: render()
    # The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as
    # its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    #  (or) for shortcut we use above two lines code
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))



def detail(request, question_id):
    #A shortcut: get_object_or_404()
    #The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments,
    #which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    #          or 
    # try:
    #   question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #   raise Http404("Question does not exist")
    # return render(request,'polls/details.html', {'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
