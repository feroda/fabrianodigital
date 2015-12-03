# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalxmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'contenuto multimediale', 'verbose_name_plural': 'contenuti multimediali'},
        ),
        migrations.AddField(
            model_name='media',
            name='tag_place',
            field=models.CharField(help_text=b'Inserire il territorio di riferimento del contenuto', max_length=64, verbose_name=b'Territorio', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='media',
            name='tag_subject',
            field=models.CharField(default='associazioni', help_text=b"Inserire i temi trattati separati da ',' (virgola)", max_length=1024, verbose_name=b'Temi'),
            preserve_default=False,
        ),
    ]
