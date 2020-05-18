from django import forms

class RecordingForm(forms.Form):
    author = forms.CharField(label='author', max_length=120)
    audio = forms.FileField(label='recording')
