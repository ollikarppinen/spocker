from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def home(request):
    title = 'Sign Up'
    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form,
    }
    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if full_name is None:
            full_name = "Nimeton"
        instance.save()
        context = {
            'title': "Thanks!"
        }

    return render(request, "home.html", context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'yourotheremail@gmail.com']
        contact_message = "%s: %s via %s" % (
            form_full_name, form_message, form_email)
        send_mail(subject, contact_message, from_email,
                  [to_email], fail_silently=True)
    #     for key, value in form.cleaned_data:
    #     cleaned_form = form.cleaned_data
    #     full_name = cleaned_form.get('full_name')
    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'forms.html', context)
