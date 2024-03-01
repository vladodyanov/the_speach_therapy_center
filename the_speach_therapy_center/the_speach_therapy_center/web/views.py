from django.shortcuts import render

def index(request):
    context = {}
    return render(request, template_name='web/index.html', context=context)
