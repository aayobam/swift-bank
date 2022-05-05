# Generated by Django 3.2.13 on 2022-05-03 14:57

import apps.common.custom_validator
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_type', '0002_alter_accounttype_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('account_no', models.CharField(blank=True, max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('transfer_limit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('identity_verification', models.FileField(help_text='upload a legal document that truely identifies you for verification', upload_to='', validators=[apps.common.custom_validator.file_validation])),
                ('verification_status', models.CharField(choices=[('failed', 'Failed'), ('success', 'Success'), ('pending', 'Pending')], default='pending', max_length=50, validators=[apps.common.custom_validator.account_no_validator])),
                ('initial_deposit_date', models.DateField(blank=True, null=True)),
                ('date_opened', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='account_type.accounttype')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'bank account',
                'verbose_name_plural': 'bank accounts',
            },
        ),
    ]
