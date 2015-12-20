# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalxmas', '0006_auto_20151217_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='author_email',
            field=models.CharField(max_length=64, verbose_name=b'email', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='author_avatar',
            field=models.URLField(verbose_name=b"link all'immagine dell'autore", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='author_name',
            field=models.CharField(max_length=64, verbose_name=b'autore', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='author_website',
            field=models.URLField(verbose_name=b"pagina web dell'autore", blank=True),
            preserve_default=True,
        ),
    ]
