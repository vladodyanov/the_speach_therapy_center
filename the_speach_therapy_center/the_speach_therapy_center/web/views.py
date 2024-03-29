from django.shortcuts import render
from django.core.mail import send_mail
from the_speach_therapy_center.web.forms import ContactForm


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
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,
                ['vdyanov@me.com'],
                fail_silently=False,
            )
            return render(request, 'web/contact_thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'web/contact.html', {'form': form})


def gallery(request):
    context = {}
    return render(request, template_name='web/gallery.html', context=context)
