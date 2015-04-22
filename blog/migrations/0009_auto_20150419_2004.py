# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150419_1938'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='\u6b63\u6587\u5185\u5bb9'),
            preserve_default=True,
        ),
    ]
