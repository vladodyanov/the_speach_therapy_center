from django.contrib.auth import forms as auth_forms

from the_speach_therapy_center.accounts.models import SpeachCenterUser


class SpeachCenterUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = SpeachCenterUser
        fields = ('email',)

    def save(self, *args, **kwargs):
        self.user = super().save(*args, **kwargs)
        return self.user


class SpeachCenterChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = SpeachCenterUser
