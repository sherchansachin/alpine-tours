from main.models import Packages
from django.shortcuts import render, get_object_or_404
from .models import Packages
from .forms import CommentForm

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def packages(request):
    packages = Packages.objects.all()
    return render(request, 'main/packages.html', {"packages":packages})


def package_detail(request, slug):
    info = get_object_or_404(Packages.objects.all(), slug=slug)
    comments = info.comments.filter(active = True)
    new_comment = None
    # if comment is posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create comment obj but do not save to the database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the commit
            new_comment.post = info
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'main/package_info.html', {'info':info,
                                                        'comments': comments,
                                                        'new_comment': new_comment,
                                                        'comment_form': comment_form})


def contact(request):
    return render(request, 'main/contact.html')