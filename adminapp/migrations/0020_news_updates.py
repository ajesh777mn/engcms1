# Generated by Django 4.0.1 on 2022-05-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0019_departments'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='-', null=True, upload_to='img', verbose_name='file')),
                ('post_date', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('details', models.TextField()),
            ],
        ),
    ]
