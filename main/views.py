from main.models import Packages
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Packages
from .forms import CommentForm, BookingForm, ContactForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse

# Create your views here.

def index(request):
    packages = Packages.objects.all()[:3]
    new_contact = None
    if request.method == 'POST':
        contactform = ContactForm(data=request.POST)
        if contactform.is_valid():
            new_contact = contactform.save(commit = False)
            new_contact.save()
            messages.success(request, 'We will reach out to you as soon as possible')
            return redirect(reverse('index'))
    else:
        contactform = ContactForm()
    return render(request, 'main/index.html',  {"packages":packages,
                                               'new_contact': new_contact,
                                               'contactform': contactform})


def packages(request):
    packages = Packages.objects.all()

    paginator = Paginator(packages, 3)
    page_num = request.GET.get('page', 1)

    try:
        packages = paginator.page(page_num)

    except PageNotAnInteger:
        packages = paginator.page(1)
        
    except EmptyPage:
        packages = paginator.page(paginator.num_pages)

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
            messages.success(request, 'Your comment is awaiting moderation!')
            return redirect(reverse('package_info', args=[info.slug]))
    else:
        comment_form = CommentForm()

    return render(request, 'main/package_info.html', {'info':info,
                                                        'comments': comments,
                                                        'new_comment': new_comment,
                                                        'comment_form': comment_form})


def contact(request):
    return render(request, 'main/contact.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking request has been send, we will contact you soon!')
            return redirect('/book-package')
    else:
        form = BookingForm()

        
    return render(request, 'main/reqform.html', {'form': form})