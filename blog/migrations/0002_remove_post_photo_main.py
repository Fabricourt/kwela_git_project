# Generated by Django 2.1.5 on 2019-04-25 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo_main',
        ),
    ]