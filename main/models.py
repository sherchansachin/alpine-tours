from decouple import Choices
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.utils.translation import activate

# Create your models here.
PACKAGE_STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)

NO_OF_PEOPLE = (
    ("1", "1 person"),
    ("2", "2 persons"),
    ("3", "3 persons"),
    ("4", "4 persons"),
    ("5", "5 persons"),
    ("6", "More than 5 persons")
)

class Packages(models.Model):
    """ model to store packages information to DB """
    package_title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=50)
    days = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=80, default="")
    activity = models.CharField(max_length=50, default="")
    elevation = models.CharField(max_length=50, default="")
    route = models.CharField(max_length=250, default="")
    seasons = models.CharField(max_length=250, default="")
    image = models.ImageField(upload_to ='package_images')
    description =  RichTextUploadingField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField(choices=PACKAGE_STATUS, default=0) # 0 -> package is unavailable

    def __str__(self):
        return self.package_title


class Comment(models.Model):
    """ model to store and accept comments for packages """
    post = models.ForeignKey(Packages, related_name='comments', on_delete=CASCADE)
    name = models.CharField(max_length=150)
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['posted_on']

    def __str__(self):
        return '{} posted a comment {}'.format(self.name, self.comment)

class RequestForm(models.Model):
    """ model for tour package request """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, unique=True)
    people = models.CharField(max_length=15, choices=NO_OF_PEOPLE)
    package_name = models.CharField(max_length=100)

    def __str__(self):
        return 'Tour package {} has been requested by {}'.format(self.package_name, self.name)

class Contact(models.Model):
    """ model for contact form """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return '{} reached with the subject {}'.format(self.name, self.subject)