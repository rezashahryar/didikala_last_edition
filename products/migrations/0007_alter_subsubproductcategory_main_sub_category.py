# Generated by Django 5.0.6 on 2024-06-01 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_subproductcategory_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsubproductcategory',
            name='main_sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_children', to='products.subproductcategory', verbose_name='دسته بندی اصلی'),
        ),
    ]