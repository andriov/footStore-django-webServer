# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180328_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='photos'),
            preserve_default=False,
        ),
    ]
