from django import forms
from django.db import models
from django.db.models import fields

from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost

        fields = ['title', 'text']

        lables = {'title':'title','text':''}