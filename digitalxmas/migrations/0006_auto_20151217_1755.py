# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('digitalxmas', '0005_auto_20151207_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='author',
            new_name='author_name',
        ),
        migrations.RemoveField(
            model_name='media',
            name='author_logo',
        ),
        migrations.AddField(
            model_name='media',
            name='author_avatar',
            field=models.ImageField(upload_to=b'', verbose_name=b"Immagine dell'autore", blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='media',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 17, 55, 41, 849372, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
