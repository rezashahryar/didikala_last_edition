# Generated by Django 5.0.6 on 2024-06-20 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_activationviaemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activationviaemail',
            name='user',
        ),
    ]
