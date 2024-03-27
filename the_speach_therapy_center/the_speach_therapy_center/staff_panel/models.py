from django.db import models
from django.utils import timezone

from the_speach_therapy_center.accounts.models import Profile


class TreatmentPlan(models.Model):
    MAX_PATIENT_NAME_LENGTH = 25

    # patient = models.CharField(
    #     max_length=MAX_PATIENT_NAME_LENGTH,
    #     blank=True,
    #     null=True,
    # )
    patient = models.ForeignKey(
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
