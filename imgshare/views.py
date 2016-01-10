from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Image
from django.shortcuts import render


def home(request):
    photos = Image.objects.all()[:5]
    context = {
        'title': 'Welcome',
        'photos': photos,
    }
    return render(request, 'home.html', context)


class UploadView(CreateView):
    model = Image
    fields = ['image']
    success_url = 'home'


class ImageView(DetailView):
    model = Image
