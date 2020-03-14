from django import forms

from webapp.models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['signature', 'upload', 'status']
