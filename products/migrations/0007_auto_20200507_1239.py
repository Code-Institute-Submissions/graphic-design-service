# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-07 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200507_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('2000x1920', '2000 x 1920'), ('1080x1920', '1080 x 1920'), ('720x720', '720 x 720'), ('720x400', '720 x 400'), ('400x400', '400 x 400'), ('200x200', '200 x 200'), ('100x100', '100 x 100')], default='1080 x 1920', max_length=15),
        ),
    ]
