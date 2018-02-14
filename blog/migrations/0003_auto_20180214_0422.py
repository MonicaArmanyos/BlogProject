# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180213_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='post',
        ),
        migrations.AddField(
            model_name='posts',
            name='tag',
            field=models.ManyToManyField(to='blog.Tags'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='picture',
            field=models.ImageField(upload_to=b'media', blank=True),
        ),
    ]
