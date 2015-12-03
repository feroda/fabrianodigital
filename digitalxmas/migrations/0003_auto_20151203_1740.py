# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('digitalxmas', '0002_auto_20151203_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='media',
            name='approved_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='media',
            name='approved_on',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
