from django import forms

class RecordingForm(forms.Form):
    recordings = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
