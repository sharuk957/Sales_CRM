# Generated by Django 3.2.9 on 2021-12-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_users_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile_number',
            field=models.BigIntegerField(unique=True),
        ),
    ]
