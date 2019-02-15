# Generated by Django 2.1.5 on 2019-02-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_delete_photoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(default='logo.jpg', upload_to='logo_pics')),
            ],
        ),
    ]