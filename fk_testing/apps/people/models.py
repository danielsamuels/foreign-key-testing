""" Models used by the people app """
from django.db import models

from cms.apps.media.models import FileRefField


class Team(models.Model):
    pass


class Person(models.Model):
    """ A person """

    teams = models.ManyToManyField(
        Team,
        null=True,
        blank=True
    )

    photo = FileRefField(
        blank=True,
        null=True
    )
