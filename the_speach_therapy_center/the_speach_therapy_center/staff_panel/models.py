from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from the_speach_therapy_center.accounts.models import Profile
from the_speach_therapy_center.core.models import UserRelatedEntity

UserModel = get_user_model()


class TreatmentPlan(models.Model):
    MAX_PATIENT_NAME_LENGTH = 25

    # therapist = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE)

    patient = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE)

    goals = models.TextField(
        blank=True
    )

    progress_notes = models.TextField(
        blank=True
    )

    next_steps = models.TextField(
        blank=True
    )

    is_completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name_plural = "Treatment Plans"

    def __str__(self):
        return f"Treatment Plan for {self.patient}"
