# Generated by Django 2.1.5 on 2019-03-14 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo_1',
        ),
    ]