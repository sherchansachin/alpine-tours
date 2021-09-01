from django.db import models
from django.db.models import fields
from .models import Comment, RequestForm, Contact
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')


class BookingForm(forms.ModelForm):
    class Meta:
        model = RequestForm
        fields = ('name', 'email', 'phone', 'people', 'package_name')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')