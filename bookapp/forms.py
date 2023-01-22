from django import forms
from . models import *

my_default_errors = {
    'required': 'To pole jest wymagane',
    'max_length': 'Wpisana wartość jest za długa'
}

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['title', 'file']
        error_messages = {
            'title': my_default_errors,
            'file': my_default_errors
        }

class PeriodForm(forms.Form):
    name = forms.CharField(label='nazwa', max_length=100, error_messages=my_default_errors)
    description = forms.CharField(label='opis', max_length=1000, widget=forms.Textarea, error_messages=my_default_errors)
    beginning = forms.IntegerField(label='początek', error_messages=my_default_errors)
    end = forms.IntegerField(label='koniec', error_messages=my_default_errors)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'author', 'period']
        error_messages = {
            'title': my_default_errors,
            'image': my_default_errors,
            'author': my_default_errors,
            'period': my_default_errors
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname']
        error_messages = {
            'name': my_default_errors,
            'surname': my_default_errors
        }
 