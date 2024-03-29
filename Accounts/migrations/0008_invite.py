# Generated by Django 3.2.9 on 2021-12-14 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_alter_account_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.account')),
            ],
        ),
    ]
