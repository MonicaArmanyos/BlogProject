# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ForbiddenWords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateField(default=datetime.datetime.now, blank=True)),
                ('picture', models.ImageField(upload_to=b'')),
                ('content', models.CharField(max_length=200)),
                ('category', models.ForeignKey(to='blog.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('comment', models.ForeignKey(to='blog.Comments')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=15)),
                ('post', models.ManyToManyField(to='blog.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=10)),
                ('created_at', models.DateField(default=datetime.datetime.now, blank=True)),
                ('is_admin', models.BooleanField()),
                ('is_blocked', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='replies',
            name='user',
            field=models.ForeignKey(to='blog.Users'),
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(to='blog.Users'),
        ),
        migrations.AddField(
            model_name='likes',
            name='post',
            field=models.ForeignKey(to='blog.Posts'),
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(to='blog.Posts'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to='blog.Users'),
        ),
        migrations.AddField(
            model_name='categories',
            name='user',
            field=models.ManyToManyField(to='blog.Users'),
        ),
    ]
