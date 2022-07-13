# Generated by Django 4.0.1 on 2022-05-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.TextField()),
                ('description', models.TextField()),
                ('pic', models.ImageField(blank=True, default='-', null=True, upload_to='img', verbose_name='file')),
            ],
        ),
        migrations.CreateModel(
            name='home_wallpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallpaper_text', models.CharField(max_length=150)),
                ('wallpaper_pic', models.ImageField(blank=True, default='-', null=True, upload_to='img', verbose_name='file')),
            ],
        ),
    ]