# Generated by Django 2.1.5 on 2019-08-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardwares', '0002_auto_20190823_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='hardware_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
