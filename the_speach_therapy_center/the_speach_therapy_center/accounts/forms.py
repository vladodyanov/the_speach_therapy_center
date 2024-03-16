from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class SpeachCenterUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

    def save(self, *args, **kwargs):
        self.user = super().save(*args, **kwargs)
        return self.user


class SpeachCenterChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
