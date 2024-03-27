from django import forms

from the_speach_therapy_center.accounts.models import Profile
from the_speach_therapy_center.staff_panel.models import TreatmentPlan


class CreateTreatmentPlanForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        fields = ['patient', 'goals', 'progress_notes', 'next_steps', 'is_completed', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = Profile.objects.all()
        self.fields['patient'].label_from_instance = lambda obj: obj.full_name or obj.user.email
