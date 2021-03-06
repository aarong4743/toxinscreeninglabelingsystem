# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170606_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneEyeDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to=b'1_Eye/')),
                ('num_eyes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TwoEyeDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to=b'2_Eyes/')),
                ('num_eyes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ZeroEyeDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to=b'0_Eyes/')),
                ('num_eyes', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='EyeDoc',
        ),
    ]
