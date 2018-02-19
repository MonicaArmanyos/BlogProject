# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='type',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='post',
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='tag',
            field=models.ManyToManyField(to='blog.Tags'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='picture',
            field=models.ImageField(upload_to=b'media', blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
