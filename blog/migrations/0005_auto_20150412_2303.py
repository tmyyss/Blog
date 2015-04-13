# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150412_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(verbose_name='\u6b63\u6587\u5185\u5bb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u6587\u7ae0\u6807\u9898'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(verbose_name=b'author', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
