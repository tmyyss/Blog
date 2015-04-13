# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150412_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='visitors',
            field=models.IntegerField(default=0, verbose_name='\u8bbf\u95ee\u91cf'),
            preserve_default=True,
        ),
    ]
