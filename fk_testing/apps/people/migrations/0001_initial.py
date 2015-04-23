# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.apps.media.models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', cms.apps.media.models.FileRefField(blank=True, to='media.File', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='teams',
            field=models.ManyToManyField(to='people.Team', null=True, blank=True),
        ),
    ]
