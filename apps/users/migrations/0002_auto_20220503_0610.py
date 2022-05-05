# Generated by Django 3.2.13 on 2022-05-03 06:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('-date_created',), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='zipcode',
            field=models.CharField(max_length=7, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
