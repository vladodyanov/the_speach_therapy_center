from django.contrib.auth import get_user_model
from django.db import models


from the_speach_therapy_center.core.models import UserRelatedEntity

UserModel = get_user_model()


class UserQuestionnaire(UserRelatedEntity, models.Model):
    MAX_COMMENTS_LENGTH = 500

    ANSWER_CHOICES = [
        ('Never', 'Never'),
        ('Rarely', 'Rarely'),
        ('Occasionally', 'Occasionally'),
        ('Frequently', 'Frequently'),
        ('Always', 'Always'),
    ]

    question_one = models.TextField(
        choices=ANSWER_CHOICES,
        null=False,
        blank=False,
        verbose_name="How often do you experience difficulty pronouncing certain sounds?",
    )

    question_two = models.TextField(
        choices=ANSWER_CHOICES,
        null=False,
        blank=False,
        verbose_name="Do you feel confident when speaking in public?"
    )

    question_three = models.TextField(
        choices=ANSWER_CHOICES,
        null=False,
        blank=False,
        verbose_name="Have you noticed any changes in your voice quality or pitch recently?"
    )

    question_four = models.TextField(
        choices=ANSWER_CHOICES,
        null=False,
        blank=False,
        verbose_name="Do you struggle with stuttering or stammering?"
    )

    question_five = models.TextField(
        choices=ANSWER_CHOICES,
        null=False,
        blank=False,
        verbose_name="Have you ever had difficulty understanding or following conversations?"
    )

    comments = models.CharField(
        max_length=MAX_COMMENTS_LENGTH,
        null=False,
        blank=False,
        verbose_name="Additional Comments/Feedback:",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
