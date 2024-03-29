from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from the_speach_therapy_center.accounts.forms import SpeachCenterUserCreationForm
from the_speach_therapy_center.accounts.models import Profile
from the_speach_therapy_center.core.view_mixins import OwnerRequiredMixin


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('getting started')


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = SpeachCenterUserCreationForm
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse('details profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def signout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(OwnerRequiredMixin, views.DetailView):
    queryset = Profile.objects \
        .prefetch_related('user') \
        .all()
    template_name = "accounts/details_profile.html"


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()

    template_name = "accounts/edit_profile.html"
    fields = ('first_name', 'last_name', 'profile_picture', 'date_of_birth', 'phone_number', 'reasons_for_therapy',
              'previous_speech_therapy_history', 'additional_notes')

    def get_success_url(self):
        return reverse('details profile', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['date_of_birth'].widget.attrs['type'] = 'date'
        return form


class ProfileStaffUpdateView(views.UpdateView):
    queryset = Profile.objects.all()

    template_name = "accounts/edit_profile_staff.html"
    fields = ('first_name', 'last_name', 'profile_picture', 'date_of_birth', 'phone_number')

    def get_success_url(self):
        return reverse('details profile', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['date_of_birth'].widget.attrs['type'] = 'date'
        return form


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/delete_profile.html'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if request.user.is_authenticated:
            logout(request)
        return response

