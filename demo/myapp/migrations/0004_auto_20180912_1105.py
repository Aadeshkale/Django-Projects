# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-12 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180912_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depart',
            name='ed',
            field=models.OneToOneField(null=True, on_delete=models.SET(10), to='myapp.Emp'),
        ),
    ]