# Generated by Django 3.1 on 2022-10-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=225)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=13)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]