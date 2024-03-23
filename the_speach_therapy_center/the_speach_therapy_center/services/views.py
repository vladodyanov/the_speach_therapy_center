from the_speach_therapy_center.accounts.models import Profile
from django.shortcuts import render

from django.urls import reverse_lazy

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
    user = request.user
    user_email = user.email
    profile = Profile.objects.get(user=request.user)
    full_name = profile.full_name
    questionnaires = UserQuestionnaire.objects.all()
    questionnaires_count = len([questionnaire for questionnaire in questionnaires])
    context = {
        'questionnaires': questionnaires,
        'questionnaires_count': questionnaires_count,
        'user_email': user_email,
        'full_name': full_name,
        }

    return render(request, template_name='services/questionnaires.html', context=context)


class CreateQuestionnaireView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = CreateQuestionnaireForm
    template_name = 'services/questionnaire_create.html'
    success_url = reverse_lazy('questionnaires_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditQuestionnaireView(views.UpdateView):
    queryset = UserQuestionnaire.objects.all()
    fields = ['question_one', 'question_two', 'question_three', 'question_four',
              'question_five', 'comments', ]
    template_name = 'services/questionnaire_edit.html'
    success_url = reverse_lazy('questionnaires_page')


class DeleteQuestionnaireView(views.DeleteView):
    queryset = UserQuestionnaire.objects.all()
    template_name = 'services/questionnaire_delete.html'
    success_url = reverse_lazy('questionnaires_page')

