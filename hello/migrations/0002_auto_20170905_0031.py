# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('accountid', models.CharField(max_length=200)),
                ('accesskey', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Credentials',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('fname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]