from django.shortcuts import render


def pediatric_service(request):
    context = {}
    return render(request, template_name='services/pediatric.html', context=context)


def adult_service(request):
    context = {}
    return render(request, template_name='services/adult.html', context=context)


def occupational_service(request):
    context = {}
    return render(request, template_name='services/occupational.html', context=context)