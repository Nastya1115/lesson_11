from myapp.models import *
from django import forms

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
