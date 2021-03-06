from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Author, Book


class AuthorForm(forms.Form):
   name = forms.CharField(label='Name', max_length=40, required=True)
   age = forms.IntegerField(label='Age', required=True)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'release_month')
        labels = {
            'author': _('Author'),
        }
        help_texts = {
            'name': _('Someone you had created already.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }


class EmailForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=240, required=True)   
    text = forms.CharField(widget=forms.Textarea, label='Your Message', required=True)    