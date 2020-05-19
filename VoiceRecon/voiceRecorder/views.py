from django.shortcuts import render
from django.http import HttpResponse
from .forms import RecordingForm
from .models import Recording
from . import pyfil
from numpy import savetxt

# Create your views here.
def index(request):
    return render(request, template_name='voiceRecorder/index.html')


def record(request):
    return HttpResponse('I think we recognise you, ')


def thanks(request):
    print("Received audio I think")
    if request.method == 'POST':
        file = request.FILES['audio']
        data = pyfil.Voice2Data(file)
        print('type of data -> ', type(data))
        author = request.POST['author']
        print('author ->', author)
        savetxt('data.csv', data, delimiter=',')
    return HttpResponse("Thanks")


def result(request):
    return render(request, template_name='voiceRecorder/result.html')