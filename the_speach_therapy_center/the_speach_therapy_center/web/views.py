from django.shortcuts import render
from django.core.mail import send_mail
from the_speach_therapy_center.web.forms import SpeachCenterContactForm


def index(request):
    context = {}
    return render(request, template_name='web/index.html', context=context)


def about(request):
    context = {}
    return render(request, template_name='web/about.html', context=context)


def location(request):
    context = {}
    return render(request, template_name='web/location.html', context=context)


def contact(request):
    if request.method == 'POST':
        form = SpeachCenterContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Message from the Speach Therapy Center',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,
                ['bevintage83@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'web/contact_thank_you.html')
    else:
        form = SpeachCenterContactForm()
    return render(request, 'web/contact.html', {'form': form})


def gallery(request):
    context = {}
    return render(request, template_name='web/gallery.html', context=context)
