from django.shortcuts import render
# Create your views here.


def about(request):
    return render(request, "about.html", {})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
