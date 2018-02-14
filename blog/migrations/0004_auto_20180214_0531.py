# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20180214_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='user_likes',
            field=models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
