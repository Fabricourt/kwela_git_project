# Generated by Django 2.1.5 on 2019-03-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo_blog',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
