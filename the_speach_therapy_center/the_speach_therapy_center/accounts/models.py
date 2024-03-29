from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models, get_user_model
from the_speach_therapy_center.accounts.managers import SpeachCenterUserManager
from datetime import datetime
from django.utils import timezone


class SpeachCenterUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = SpeachCenterUserManager()


UserModel = get_user_model()


class Profile(models.Model):

    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30
    MAX_PHONE_NUMBER_LENGTH = 15
    MAX_TEXT_LENGTH = 500

    TYPE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    REASONS_FOR_SPEACH_THERAPY = [
        ('cognitive (intellectual, thinking) developmental delays', 'cognitive (intellectual, thinking) developmental '
                                                                    'delays'),
        ('weak oral muscles', 'weak oral muscles'),
        ('cleft lip or palate', 'cleft lip or palate'),
        ('autism', 'autism'),
        ('motor planning problems', 'motor planning problems'),
        ('articulation problems', 'articulation problems'),
        ('other', 'other'),
    ]

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=MAX_PHONE_NUMBER_LENGTH,
        blank=True,
        null=True)

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    reasons_for_therapy = models.TextField(
        choices=REASONS_FOR_SPEACH_THERAPY,
        blank=True,
        null=True
    )

    previous_speech_therapy_history = models.CharField(
        choices=TYPE_CHOICES,
        null=True,
        blank=True,
    )

    additional_notes = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        SpeachCenterUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        today = datetime.now().date()
        age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

        return self.first_name or self.last_name
