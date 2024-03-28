from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
from the_speach_therapy_center.core.models import UserRelatedEntity

UserModel = get_user_model()


class Appointment(UserRelatedEntity, models.Model):
    SERVICE_CHOICES = (
        ("Pediatric speech service", "Pediatric speech service"),
        ("Adult speech service", "Adult speech service"),
        ("Occupational therapy service", "Occupational therapy service"),

    )
    TIME_CHOICES = (
        ("3 PM", "3 PM"),
        ("4 PM", "4 PM"),
        ("5 PM", "5 PM"),
        ("6 PM", "6 PM"),
        ("7 PM", "7 PM"),
    )

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        default="Pediatric speech service"
    )

    day = models.DateField(
        default=datetime.now
    )

    time = models.CharField(
        max_length=10,
        choices=TIME_CHOICES,
        default="3 PM"
    )

    time_ordered = models.DateTimeField(
        default=datetime.now,
        blank=True
    )

    def __str__(self):
        return f"{self.user.email} | day: {self.day} | time: {self.time}"


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

    comments = models.TextField(
        max_length=MAX_COMMENTS_LENGTH,
        null=False,
        blank=False,
        verbose_name="Additional Comments/Feedback:",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
