# Generated by Django 3.2.13 on 2022-05-03 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_type', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounttype',
            options={'ordering': ('date_created',), 'verbose_name': 'account type', 'verbose_name_plural': 'account types'},
        ),
    ]
