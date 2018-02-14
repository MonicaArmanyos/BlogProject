# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20180214_0531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='user_likes',
        ),
        migrations.AddField(
            model_name='posts',
            name='userLikes',
            field=models.ManyToManyField(related_name='userLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
