"""Models used by the static media management application."""
from django.db import models


class File(models.Model):
    pass


class FileRefField(models.ForeignKey):

    """A foreign key to a File, constrained to only select image files."""

    def __init__(self, **kwargs):
        kwargs["to"] = File
        # kwargs["to"] = 'media.File'
        super(FileRefField, self).__init__(**kwargs)
