# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-28 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170705_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='CommentDate',
            field=models.DateTimeField(auto_now=True, verbose_name='Comment Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='GuestUserKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.GuestUser', verbose_name='Guest User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='PostKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='GuestUserKey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.GuestUser', verbose_name='Guest User'),
        ),
        migrations.AlterField(
            model_name='like',
            name='LikeDate',
            field=models.DateTimeField(auto_now=True, verbose_name='Like Date'),
        ),
        migrations.AlterField(
            model_name='like',
            name='PostKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='GuestUserKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.GuestUser', verbose_name='Guest User'),
        ),
        migrations.AlterField(
            model_name='post',
            name='PostImageURL',
            field=models.URLField(max_length=250, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='PostText',
            field=models.TextField(verbose_name='Post Text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='PostTitle',
            field=models.CharField(max_length=250, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='PostVisible',
            field=models.BooleanField(default=False, verbose_name='Post Visible?'),
        ),
    ]
