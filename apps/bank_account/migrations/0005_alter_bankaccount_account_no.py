# Generated by Django 3.2.13 on 2022-05-10 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0004_alter_bankaccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_no',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
