# Generated by Django 2.1.5 on 2019-02-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(upload_to='contact_pics'),
        ),
    ]