# Generated by Django 3.2.13 on 2022-05-05 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankaccount',
            options={'verbose_name': 'Bank account', 'verbose_name_plural': 'Bank accounts'},
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='initial_deposit_date',
        ),
    ]