# Generated by Django 3.1 on 2022-10-18 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wesapp', '0007_auto_20221018_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='header_image',
        ),
    ]