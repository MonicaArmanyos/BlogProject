# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='ForbiddenWords',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='post',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='category',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
        migrations.RemoveField(
            model_name='replies',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='replies',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='post',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.DeleteModel(
            name='Replies',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
