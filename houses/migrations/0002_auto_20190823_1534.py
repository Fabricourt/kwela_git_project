# Generated by Django 2.1.5 on 2019-08-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='house',
            name='House_type',
        ),
        migrations.DeleteModel(
            name='House_type',
        ),
        migrations.AddField(
            model_name='house',
            name='bedroom',
            field=models.ManyToManyField(help_text='Select The kind of House Your Posting your', to='houses.Bedroom'),
        ),
    ]