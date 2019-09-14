# Generated by Django 2.1.5 on 2019-09-12 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]
