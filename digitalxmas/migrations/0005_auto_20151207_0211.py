# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('digitalxmas', '0004_auto_20151205_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='dedication',
            field=models.TextField(default=b'', verbose_name=b'Dedica', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='approved_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='approved_on',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='url',
            field=models.URLField(unique=True),
            preserve_default=True,
        ),
    ]
