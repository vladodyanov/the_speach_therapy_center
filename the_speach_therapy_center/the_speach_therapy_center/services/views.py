from django.shortcuts import render


def getting_started(request):
    user = request.user  # Assuming user is authenticated
    user_email = user.email
    context = {
        'user_email': user_email,
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


