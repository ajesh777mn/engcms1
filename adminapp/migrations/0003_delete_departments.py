# Generated by Django 4.0.1 on 2022-05-09 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_departments_dept_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='departments',
        ),
    ]
