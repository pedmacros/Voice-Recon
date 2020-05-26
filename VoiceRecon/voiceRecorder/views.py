import numpy
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import pyfil
from .models import Author


# Create your views here.
def index(request):
    return render(request, template_name='voiceRecorder/index.html')


def train(request):
    return HttpResponse('Training triggered ')


def thanks(request):
    print("Received audio I think")
    if request.method == 'POST':
        file = request.FILES['audio']
        data = pyfil.Voice2Data(file)
        author = request.POST['author']
        author = matchAuthor(author)
        data = numpy.append(data, author)
        print(data)
        print(len(data))
        data = data.reshape(1, data.shape[0])

        f = open('datos.csv', 'ab')
        numpy.savetxt(f, data, delimiter=',')
        f.close()
        print('Successfully added record')
    return HttpResponseRedirect('/voiceRecorder/')


def result(request):
    if request.method == 'POST':
        file = request.FILES['testerAudio']
        data = pyfil.Voice2Data(file)
        data = data.reshape(1, data.shape[0])

        f = open('guess.csv', 'ab')
        numpy.savetxt(f, data, delimiter=',')
        f.close()
        print('Successfully added record')
    return render(request, template_name='voiceRecorder/result.html')


def matchAuthor(author):
    try:

        currentAuthor = Author.objects.get(author=author)
        print(author+' recognised')
    except Author.DoesNotExist:
        print("New author is here: "+author)
        currentAuthor = Author(author=author)
        currentAuthor.save()

    result = currentAuthor.pk
    return result
