from decouple import Choices
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.deletion import CASCADE
from django.utils.translation import activate

# Create your models here.
PACKAGE_STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)

class Packages(models.Model):
    """ model to store packages information to DB """
    package_title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=50)
    days = models.CharField(max_length=50)
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