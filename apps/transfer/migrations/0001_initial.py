# Generated by Django 3.2.13 on 2022-05-07 23:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('receiver_account', models.CharField(max_length=10)),
                ('receiver_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('failed', 'Failed'), ('success', 'Success'), ('pending', 'Pending')], max_length=20)),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_account.bankaccount')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
