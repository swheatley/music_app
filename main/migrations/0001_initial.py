# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name=b'last name', blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('album_id', models.IntegerField(serialize=False, primary_key=True)),
                ('album_title', models.CharField(max_length=255, null=True)),
                ('album_date_released', models.IntegerField(null=True, blank=True)),
                ('album_image', models.ImageField(upload_to=b'album_images')),
            ],
            options={
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.IntegerField(serialize=False, primary_key=True)),
                ('artist_url', models.URLField(max_length=255, null=True, blank=True)),
                ('artist_name', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_bio', models.TextField(null=True, blank=True)),
                ('artist_location', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_website', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_handle', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_id', models.IntegerField(null=True, blank=True)),
                ('genre_parent_id', models.IntegerField(null=True, blank=True)),
                ('genre_title', models.CharField(max_length=255, null=True, blank=True)),
                ('genre_slug', models.SlugField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('track_id', models.IntegerField(null=True, blank=True)),
                ('track_title', models.CharField(max_length=255, null=True)),
                ('track_file', models.FileField(upload_to=b'tracks')),
                ('album', models.ForeignKey(to='main.Albums', null=True)),
                ('genre', models.ForeignKey(to='main.Genres', null=True)),
            ],
            options={
                'verbose_name_plural': 'Tracks',
            },
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(to='main.Artist', null=True),
        ),
    ]
