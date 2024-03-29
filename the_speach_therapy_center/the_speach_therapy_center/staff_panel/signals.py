from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from the_speach_therapy_center.staff_panel.models import TreatmentPlan

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_treatment_plan(sender, instance, created, **kwargs):
    if created:
        TreatmentPlan.objects.create(user=instance)
