from django.http import HttpResponseForbidden


def patient_user(user):
    return not user.is_staff


def patient_user_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if patient_user(request.user):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access this page.")

    return _wrapped_view


def staff_user(user):
    return user.is_staff


def staff_user_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if staff_user(request.user):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access this page.")

    return _wrapped_view
