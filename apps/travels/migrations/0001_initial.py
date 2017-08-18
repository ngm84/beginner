# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-18 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0002_auto_20170818_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('trip_start', models.DateTimeField()),
                ('trip_end', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('travelers', models.ManyToManyField(related_name='trips_travelers', to='loginreg.User')),
                ('trip_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User')),
            ],
        ),
    ]
