# Generated by Django 3.1 on 2022-10-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wesapp', '0020_auto_20221021_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]