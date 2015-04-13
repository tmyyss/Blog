# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150412_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_time',
            field=models.DateTimeField(null=True, verbose_name='\u53d1\u5e03\u65f6\u95f4', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
