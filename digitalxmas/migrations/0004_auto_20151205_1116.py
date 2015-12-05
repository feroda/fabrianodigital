# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalxmas', '0003_auto_20151203_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='author_website',
            field=models.URLField(verbose_name=b"Pagina web dell'autore", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='author',
            field=models.CharField(max_length=64, verbose_name=b'Autore', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='author_logo',
            field=models.ImageField(upload_to=b'', verbose_name=b"Logo dell'autore", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.TextField(default=b'', verbose_name=b'Descrizione', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='tag_place',
            field=models.CharField(default=b'Fabriano', help_text=b'Territorio di riferimento del contenuto', max_length=64, verbose_name=b'Territorio', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='tag_subject',
            field=models.CharField(help_text=b"Temi trattati separati da ',' (virgola)", max_length=1024, verbose_name=b'Temi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(max_length=64, verbose_name=b'Titolo'),
            preserve_default=True,
        ),
    ]
