from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import handlers

# Create your views here.
def index(request):
    return render(request, template_name='voiceRecorder/index.html')


def train(request):
    return HttpResponse('Training triggered ')


def thanks(request):
    print("Received audio file")
    if request.method == 'POST':
        files = request.FILES.getlist('audio')
        author = request.POST['author']
        handlers.trainingHandler(files, author)
    return HttpResponseRedirect('/voiceRecorder/')


def result(request):
    if request.method == 'POST':
        file = request.FILES['testerAudio']
        handlers.resultHandler(file)
    return render(request, template_name='voiceRecorder/result.html')



