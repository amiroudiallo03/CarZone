# Generated by Django 4.0.1 on 2022-01-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carzoneapp', '0017_alter_car_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='about_image')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('icone', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('logo', models.FileField(upload_to='logo_website')),
                ('copyrights', models.CharField(max_length=50)),
                ('title_service', models.CharField(max_length=50)),
                ('description_service', models.TextField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Website',
                'verbose_name_plural': 'Websites',
            },
        ),
    ]
