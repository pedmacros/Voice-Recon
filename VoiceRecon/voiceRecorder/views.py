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
        print('type of data -> ', type(data))
        author = request.POST['author']
        author = author.strip()
        author = author.lower()
        print('author ->', author)
        data = ''.join(str(e) + ',' for e in data)
        data += author
        print(data)
        file = open('data.csv', 'a')
        file.write(data + '\n')
        file.close()
        # savetxt('data.csv', data, delimiter=',')
    return HttpResponseRedirect('/voiceRecorder/')


def result(request):
    return render(request, template_name='voiceRecorder/result.html')
