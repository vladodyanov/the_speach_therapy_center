from django.shortcuts import render
from the_speach_therapy_center.accounts.models import Profile


def getting_started(request):
    user = request.user
    user_email = user.email
    profile = Profile.objects.get(user=request.user)
    full_name = profile.full_name
    context = {
        'user_email': user_email,
        'full_name': full_name,
    }
    return render(request, template_name='services/getting_started.html', context=context)


def pediatric_service(request):
    context = {}
    return render(request, template_name='services/pediatric.html', context=context)


def adult_service(request):
    context = {}
    return render(request, template_name='services/adult.html', context=context)


def occupational_service(request):
    context = {}
    return render(request, template_name='services/occupational.html', context=context)


