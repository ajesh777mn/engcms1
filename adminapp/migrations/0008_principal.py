# Generated by Django 4.0.1 on 2022-05-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_rename_useful_links_useful_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='-', null=True, upload_to='img', verbose_name='file')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=150)),
                ('welcome_note', models.CharField(max_length=500)),
                ('profile_details', models.TextField()),
            ],
        ),
    ]
