"""Core models used by the CMS."""
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Page(models.Model):

    content_type = models.ForeignKey(
        ContentType,
    )


class ContentBase(models.Model):

    page = models.OneToOneField(
        Page,
    )

    class Meta:
        abstract = True
