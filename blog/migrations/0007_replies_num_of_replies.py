# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180217_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='replies',
            name='num_of_replies',
            field=models.IntegerField(default=0),
        ),
    ]
