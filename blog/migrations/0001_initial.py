# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='CategoryUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='blog.Categories')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('num_of_replies', models.IntegerField(default=0)),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('comment', models.ForeignKey(to='blog.Comments')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=15)),
                ('post', models.ManyToManyField(related_name='post_tags', to='blog.Posts')),
            ],
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categories',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='blog.CategoryUser'),
        ),
    ]
