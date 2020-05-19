from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RecordingForm
from .models import Recording
from . import pyfil
from numpy import savetxt
from .VoiceNetwork import trainNetwork


# Create your views here.
def index(request):
    return render(request, template_name='voiceRecorder/index.html')


def train(request):
    trainNetwork()
    return HttpResponse('Training triggered ')


def thanks(request):
    print("Received audio I think")
    if request.method == 'POST':
        file = request.FILES['audio']
        data = pyfil.Voice2Data(file).tolist()
        author = request.POST['author']
        author = author.strip()
        author = author.lower()
        print('author ->', author)
        data = ''.join(str(e) + ',' for e in data)
        data += author
        file = open('data.csv', 'a')
        file.write(data + '\n')
        file.close()
        print('Successfully added record')
    return HttpResponseRedirect('/voiceRecorder/')


def result(request):
    return render(request, template_name='voiceRecorder/result.html')
