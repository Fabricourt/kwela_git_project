# Generated by Django 2.1.5 on 2019-02-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20190216_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]