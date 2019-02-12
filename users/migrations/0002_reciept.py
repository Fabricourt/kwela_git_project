# Generated by Django 2.1.5 on 2019-01-24 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reciept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reciept_No', models.CharField(max_length=200, null=True)),
                ('Bank', models.CharField(max_length=200, null=True)),
                ('Bank_branch', models.CharField(max_length=200, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('Mpesa_message', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('Paid', models.IntegerField(null=True)),
                ('Balance', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]