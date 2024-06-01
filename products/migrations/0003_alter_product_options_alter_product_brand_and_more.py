# Generated by Django 5.0.6 on 2024-05-31 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_inventory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_date',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='products.brand', verbose_name='برند'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='colors', to='products.color', verbose_name='رنگ'),
        ),
    ]