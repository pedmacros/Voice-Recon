from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, template_name='voiceRecorder/index.html')


def record(request):
    return HttpResponse('I think we recognise you, ')


def thanks(request):
    print("Received audio I think")
    return HttpResponse("Thanks")


def result(request):
    return HttpResponse("This is the result")
