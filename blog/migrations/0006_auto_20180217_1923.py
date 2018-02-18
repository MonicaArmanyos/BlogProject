# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180217_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='replies',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
