# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalxmas', '0008_auto_20151220_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='email_to',
            field=models.CharField(default=b'', max_length=1024, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='media',
            name='is_private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='tag_subject',
            field=models.CharField(default=b'', help_text=b"Temi trattati separati da ',' (virgola)", max_length=1024, verbose_name=b'Temi', blank=True),
            preserve_default=True,
        ),
    ]
