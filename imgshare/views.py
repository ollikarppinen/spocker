from django.views.generic.edit import CreateView
from .models import Image
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def home(request):
    images = Image.objects.all()[::-1]
    context = {
        'images': images,
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
    context['username'] = user.username
    return render(request, 'imgshare/userprofile.html', context)
