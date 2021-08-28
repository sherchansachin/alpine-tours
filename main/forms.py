from django.db import models
from django.db.models import fields
from .models import Comment, RequestForm
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')


class BookingtForm(forms.ModelForm):
    class Meta:
        model = RequestForm
        fields = ('name', 'email', 'phone', 'people', 'package_name')