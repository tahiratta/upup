# Generated by Django 2.0.2 on 2018-03-21 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('about_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('about_title', models.CharField(max_length=20)),
                ('about_content', models.CharField(max_length=7000)),
                ('mission_image', models.ImageField(upload_to='')),
                ('mission_content', models.CharField(max_length=2000)),
                ('value_image', models.ImageField(upload_to='')),
                ('value_content', models.CharField(max_length=2000)),
                ('vision_image', models.ImageField(upload_to='')),
                ('vision_content', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'about',
            },
        ),
        migrations.CreateModel(
            name='Image_slider',
            fields=[
                ('islider_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('islider_title', models.CharField(max_length=200)),
                ('islider_description', models.CharField(max_length=200)),
                ('islider_image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'image_slider',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('menu_title', models.CharField(max_length=200)),
                ('show_in_menu', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'product',
            },
        ),
        migrations.CreateModel(
            name='Sub_menu',
            fields=[
                ('sub_menu_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sub_menu_title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmc.Menu')),
            ],
            options={
                'verbose_name_plural': 'sub_menu',
            },
        ),
        migrations.CreateModel(
            name='Sub_of_sub_menu',
            fields=[
                ('sub_of_sub_menu_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sub_of_sub_menu_title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmc.Sub_menu')),
            ],
            options={
                'verbose_name_plural': 'sub_of_sub_menu',
            },
        ),
        migrations.CreateModel(
            name='Sub_product',
            fields=[
                ('sub_product_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sub_product_title', models.CharField(max_length=200)),
                ('sub_product_image', models.ImageField(upload_to='')),
                ('sub_product_content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmc.Product')),
            ],
            options={
                'verbose_name_plural': 'Sub_product',
            },
        ),
        migrations.CreateModel(
            name='Video_slider',
            fields=[
                ('vslider_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('vslider_title', models.CharField(max_length=200)),
                ('vslider_description', models.CharField(max_length=200)),
                ('vslider_video', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'video_slider',
            },
        ),
    ]
