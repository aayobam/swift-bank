# Generated by Django 3.2.13 on 2022-05-07 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='zipcode',
            field=models.CharField(max_length=7, null=True),
        ),
    ]