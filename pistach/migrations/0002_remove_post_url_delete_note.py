# Generated by Django 4.1 on 2022-11-10 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pistach', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
