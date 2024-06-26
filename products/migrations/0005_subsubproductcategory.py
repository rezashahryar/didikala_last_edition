# Generated by Django 5.0.6 on 2024-06-01 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_brand_options_alter_color_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSubProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(unique=True, verbose_name='مسیر یو ار ال')),
                ('main_sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.subproductcategory', verbose_name='دسته بندی اصلی')),
            ],
        ),
    ]
