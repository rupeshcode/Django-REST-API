# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170623_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photos',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='photos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
