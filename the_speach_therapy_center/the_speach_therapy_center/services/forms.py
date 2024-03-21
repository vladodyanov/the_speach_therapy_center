from django import forms

from the_speach_therapy_center.services.models import UserQuestionnaire


class CreateQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = UserQuestionnaire
        fields = ['name', 'question_one', 'question_two', 'question_three', 'question_four',
                  'question_five']