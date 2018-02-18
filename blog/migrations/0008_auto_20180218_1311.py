# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_replies_num_of_replies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replies',
            name='num_of_replies',
        ),
        migrations.AddField(
            model_name='comments',
            name='num_of_replies',
            field=models.IntegerField(default=0),
        ),
    ]
