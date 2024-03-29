# Generated by Django 3.2.9 on 2021-12-18 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=250)),
                ('owner_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contactdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_num', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.person')),
            ],
        ),
    ]
