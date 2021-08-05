from main.models import Packages
from django.shortcuts import render, get_object_or_404
from .models import Packages

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def packages(request):
    packages = Packages.objects.all()
    return render(request, 'main/packages.html', {"packages":packages})

def package_detail(request, slug):
    info = get_object_or_404(Packages, slug=slug)
    return render(request, 'main/package_info.html', {'info':info})