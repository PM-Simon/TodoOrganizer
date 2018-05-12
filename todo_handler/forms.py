from django import forms
from todo_handler.models import Todo
from django.forms import DateInput, TextInput


class Form_new_todo(forms.ModelForm):
    class Meta:
        model = Todo
        labels = {
            'title': 'Titel', 'description': 'Beschreibung', 'deadline': 'Deadline', 'progress': 'Fortschritt',
        }
        fields = ('title', 'description', 'deadline', 'progress', )
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'style': 'width: 200px', 'type': 'text'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Beschreiben Sie ihr TODO...'}),
            'deadline': DateInput(attrs={'class': 'form-control', 'style': 'width: 200px', 'type': 'date'}),
            'progress': TextInput(attrs={'class': 'form-control', 'style': 'width: 200px', 'type': 'number', 'min': '0', 'max': '100'}),
        }
