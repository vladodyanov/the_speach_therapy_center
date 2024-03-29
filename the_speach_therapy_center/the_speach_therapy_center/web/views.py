from django.shortcuts import render

from templates.web.forms import ContactForm


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
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, template_name='web/contact.html', context=context)


def gallery(request):
    context = {}
    return render(request, template_name='web/gallery.html', context=context)
