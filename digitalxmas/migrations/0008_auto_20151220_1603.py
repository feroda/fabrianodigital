# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalxmas', '0007_auto_20151220_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='author_email',
            field=models.EmailField(max_length=75, verbose_name=b'email', blank=True),
            preserve_default=True,
        ),
    ]
