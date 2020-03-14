from django import forms

from webapp import models
from webapp.models import File


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['signature', 'upload', 'status']
        exclude = ['created_at', 'author']


class AnonymousFileForm(forms.ModelForm ):
    class Meta:
        model = File
        fields = ['signature', 'upload', 'status']
        exclude = ['created_at', 'author', 'status']
