# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-09 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0017_auto_20190308_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientbill',
            name='client_comment',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Client comments'),
        ),
    ]