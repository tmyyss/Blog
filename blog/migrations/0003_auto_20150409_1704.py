# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150328_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='agree_num',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='not_agree_num',
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'created time', verbose_name=b'blog create time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_time',
            field=models.DateTimeField(help_text=b'published time', null=True, verbose_name=b'blog published time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(help_text=b'blog context', verbose_name=b'blog context'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text=b'blog title', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(verbose_name=b'author', to=settings.AUTH_USER_MODEL, help_text=b'author'),
            preserve_default=True,
        ),
    ]
