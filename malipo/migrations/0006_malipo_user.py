# Generated by Django 2.1.5 on 2019-02-02 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('malipo', '0005_auto_20190202_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='malipo',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]