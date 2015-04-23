from django.db import models

from cms.apps.media.models import FileRefField
from cms.apps.pages.models import ContentBase


class NewsFeed(ContentBase):
    pass


class Article(models.Model):

    news_feed = models.ForeignKey(
        NewsFeed,
    )

    image = FileRefField(
        blank=True,
        null=True,
    )
