# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='CommentDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='like',
            name='GuestUserKey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.GuestUser'),
        ),
    ]
