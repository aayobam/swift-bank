# Generated by Django 4.2.7 on 2024-01-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_customuser_birth_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="country",
            field=models.CharField(
                choices=[("", "Select Country..."), ("nigeria", "Nigeria")],
                default="nigeria",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="gender",
            field=models.CharField(
                choices=[
                    ("", "Select User Gender..."),
                    ("male", "Male"),
                    ("female", "Female"),
                    ("others", "Others"),
                ],
                default="male",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("", "Select User Role..."),
                    ("customer", "Customer"),
                    ("admin", "Admin"),
                    ("account officer", "Account Officer"),
                ],
                default="admin",
                max_length=50,
            ),
        ),
    ]
