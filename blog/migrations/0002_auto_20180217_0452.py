# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='post',
            field=models.ManyToManyField(related_name='post_tags', to='blog.Posts'),
        ),
    ]
