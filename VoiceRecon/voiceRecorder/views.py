from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import RecordingForm

# Create your views here.
def index(request):
    return render(request, template_name='voiceRecorder/index.html')


def record(request):
    return HttpResponse('I think we recognise you, ')


def thanks(request):
    print("Received audio I think")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecordingForm(request.POST, request.FILES)
        print(type(request.FILES['recording']))
        data = request.FILES['recording']
        print(data)
        # check whether it's valid:
        if form.is_valid():
            print("It is valid bro")
            print(form.cleaned_data['author'])
    return HttpResponse("Thanks")


def result(request):
    return render(request, template_name='voiceRecorder/result.html')