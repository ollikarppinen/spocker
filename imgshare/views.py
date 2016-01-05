from django.shortcuts import render


def home(request):
    title = 'Welcome'
    context = {
        'title': title,
    }

    return render(request, "home.html", context)

