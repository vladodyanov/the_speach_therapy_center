from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class UserRelatedEntity(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True