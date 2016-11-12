# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 03:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('subject', models.TextField()),
                ('photographer', models.CharField(max_length=200)),
                ('architect', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('rights', models.CharField(max_length=200)),
                ('directory_name', models.CharField(max_length=200)),
                ('file_format', models.CharField(max_length=200)),
                ('file_name', models.CharField(max_length=200)),
                ('has_people', models.BooleanField()),
                ('provenance', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]