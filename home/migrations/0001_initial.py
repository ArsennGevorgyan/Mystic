# Generated by Django 5.0.1 on 2024-01-30 22:40

import helpers.media_upload
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=helpers.media_upload.upload_about_us)),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to=helpers.media_upload.upload_chef)),
            ],
        ),
        migrations.CreateModel(
            name='FollowUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=helpers.media_upload.upload_why_choose_us)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('opening_hours', models.CharField(max_length=100)),
                ('follow_us', models.ManyToManyField(blank=True, related_name='contact_us', to='home.followus')),
            ],
        ),
    ]
