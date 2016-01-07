from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Image


def home(request):
    title = 'Welcome'
    context = {
        'title': title,
    }
    return render(request, "home.html", context)


def upload(request):
    title = 'Upload'
    context = {
        'title': title,
    }
    return render(request, 'upload.html', context)


class UploadView(CreateView):
    model = Image


class Gallery(DetailView):
    model = Image
