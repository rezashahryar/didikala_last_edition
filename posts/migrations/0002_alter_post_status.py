# Generated by Django 5.0.6 on 2024-05-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('p', 'Published'), ('d', 'Draft')], default='p', max_length=2),
        ),
    ]