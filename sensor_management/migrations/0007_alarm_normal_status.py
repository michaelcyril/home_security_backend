# Generated by Django 5.0.6 on 2024-07-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_management', '0006_alter_intruderattempt_pir_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='normal_status',
            field=models.IntegerField(default=0),
        ),
    ]
