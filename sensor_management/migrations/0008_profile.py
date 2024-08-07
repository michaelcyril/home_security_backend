# Generated by Django 5.0.6 on 2024-07-18 04:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_management', '0007_alarm_normal_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('server_ip', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
