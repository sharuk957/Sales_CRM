# Generated by Django 3.2.9 on 2021-12-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_alter_users_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='company_name',
            field=models.CharField(max_length=250),
        ),
    ]
