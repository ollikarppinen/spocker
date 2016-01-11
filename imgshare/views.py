from django.views.generic.edit import CreateView
from .models import Image
from django.shortcuts import render, get_object_or_404
from math import ceil
from django.contrib.auth.models import User


def home(request):
    image_limit = 20
    row_width = 4
    if Image.objects.count() < image_limit:
        image_limit = Image.objects.count()
    rows = ceil(image_limit / row_width)
    latest_images = list()
    images = Image.objects.all()[::-1]
    for r in range(rows):
        start = r * row_width
        end = start + row_width
        if end > image_limit:
            end = image_limit
        latest_images.append(list(images[start: end]))
    context = {
        'latest_images': latest_images,
    }
    return render(request, 'home.html', context)


class UploadView(CreateView):
    model = Image
    fields = ['image']


def image(request, pk):
    try:
        image = Image.objects.get(pk=pk)
        context = {
            'image': image
        }
        return render(request, 'imgshare/image.html', context)
    except:
        return render(request, 'imgshare/image_not_found.html', {})


def gallery(request):
    return render(request, 'imgshare/gallery.html', {})


def user_view(request, username):
    context = {}
    user = get_object_or_404(User, username=username)
    context['username'] = username
    return render(request, 'imgshare/userprofile.html', context)
