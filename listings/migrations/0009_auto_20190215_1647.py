# Generated by Django 2.1.5 on 2019-02-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20190215_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='kwela',
            field=models.ImageField(default='kwela.jpg', upload_to='kwela_pics'),
        ),
    ]
