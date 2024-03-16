from django.shortcuts import render


def index(request):
    context = {}
    return render(request, template_name='web/index.html', context=context)


def about(request):
    context = {}
    return render(request, template_name='web/about.html', context=context)


def contact(request):
    context = {}
    return render(request, template_name='web/contact.html', context=context)


def gallery(request):
    context = {}
    return render(request, template_name='web/gallery.html', context=context)

