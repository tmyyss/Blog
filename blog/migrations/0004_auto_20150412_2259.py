# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150409_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'blog create time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_time',
            field=models.DateTimeField(null=True, verbose_name=b'blog published time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(verbose_name=b'blog context'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
