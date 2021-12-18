# Generated by Django 3.2.9 on 2021-12-18 07:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=250)),
                ('owner_email', models.EmailField(max_length=254)),
                ('mobile_num', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), null=True, size=None)),
                ('email', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=55), null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('product_code', models.IntegerField()),
                ('price', models.FloatField()),
                ('tax', models.FloatField()),
                ('units', models.IntegerField()),
            ],
        ),
    ]
