# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalxmas', '0009_auto_20151223_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='email_sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
