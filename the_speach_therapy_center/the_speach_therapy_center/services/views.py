from the_speach_therapy_center.accounts.models import Profile
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from the_speach_therapy_center.services.forms import CreateQuestionnaireForm
from the_speach_therapy_center.services.models import UserQuestionnaire


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


def questionnaires_page(request):
    questionnaires = UserQuestionnaire.objects.all()
    questionnaires_count = len([questionnaire for questionnaire in questionnaires])
    context = {'questionnaires': questionnaires,
               'questionnaires_count': questionnaires_count}

    return render(request, template_name='services/questionnaires.html', context=context)


# class CreateQuestionnaireView(auth_mixin.LoginRequiredMixin, views.CreateView):
#     form_class = CreateQuestionnaireForm
#     template_name = "services/questionnaire_create.html"
#
#     def get_success_url(self):
#         return reverse("details pet", kwargs={
#             "username": "Doncho",
#             "questions_slug": self.object.slug,
#         })
#
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class=form_class)
#
#         form.instance.user = self.request.user
#         return form

class CreateQuestionnaireView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = CreateQuestionnaireForm
    template_name = 'services/questionnaire_create.html'
    success_url = reverse_lazy('questionnaires_page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class DetailsQuestionnaireView(views.DetailView):
    pass
    # queryset = Car.objects.all()
    # fields = ('type', 'model', 'year', 'image_url', 'price')
    # template_name = 'car/car-details.html'


class EditQuestionnaireView(views.UpdateView):
    pass
    # queryset = Car.objects.all()
    # fields = ('type', 'model', 'year', 'image_url', 'price')
    # template_name = 'car/car-edit.html'
    # success_url = reverse_lazy('catalogue')


class DeleteQuestionnaireView(views.DeleteView):
    pass
    # queryset = Car.objects.all()
    # template_name = 'car/car-delete.html'
    # form_class = modelform_factory(Car, fields=('type', 'model', 'year', 'image_url', 'price'))
    # success_url = reverse_lazy('catalogue')
    #
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['instance'] = self.object
    #     return kwargs
