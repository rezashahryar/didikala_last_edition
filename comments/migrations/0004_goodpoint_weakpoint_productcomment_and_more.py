# Generated by Django 5.0.6 on 2024-06-02 06:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_alter_postcomment_options'),
        ('products', '0009_alter_setproductproperty_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_point', models.CharField(max_length=255, verbose_name='ویژگی خوب')),
            ],
        ),
        migrations.CreateModel(
            name='WeakPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weak_point', models.CharField(max_length=255, verbose_name='ویژگی بد')),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
                ('suggest_buy_product', models.CharField(choices=[('i_s', 'پیشنهاد میکنم'), ('i_d_s', 'خیر پیشنهاد نمی کنم'), ('n_i', 'نظری ندارم')], max_length=20, verbose_name='پیشنهاد برای خرید')),
                ('comment_status', models.CharField(choices=[('w', 'Waiting'), ('a', 'Approved'), ('na', 'Not Approved')], default='w', max_length=15)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product', verbose_name='محصول')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کامنت محصولات',
                'verbose_name_plural': 'کامنت های محصولات',
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.CreateModel(
            name='ProductCommentScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(choices=[('l', 'like'), ('dl', 'dislike')], max_length=3)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='comments.productcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_points', to='comments.productcomment', verbose_name='کامنت')),
                ('good_point', models.ManyToManyField(related_name='good_points', to='comments.goodpoint', verbose_name='ویژگی های خوب')),
                ('weak_point', models.ManyToManyField(related_name='weak_points', to='comments.weakpoint', verbose_name='ویژگی های بد')),
            ],
        ),
    ]
