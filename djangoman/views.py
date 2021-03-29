from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def greet(request):
    return HttpResponse("hi")

def index(request):
    # q = Question.objects.all()
    return render(request, 'index.html')
    # return render(request, 'index.html', {'data': q})





