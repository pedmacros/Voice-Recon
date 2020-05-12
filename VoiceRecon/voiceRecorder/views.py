from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, template_name='voiceRecorder/index.html')


def record(request):
    return HttpResponse("This will be the recording menu")


def result(request):
    return HttpResponse("This is the result")
