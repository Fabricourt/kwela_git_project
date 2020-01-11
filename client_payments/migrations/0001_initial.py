# Generated by Django 2.1.5 on 2020-01-05 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('buying_price', models.IntegerField(default=0)),
                ('amount_paid', models.IntegerField(default=0)),
                ('total_amount_paid', models.IntegerField(default=0)),
                ('current_balance', models.IntegerField(default=0)),
                ('reciept_number', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('is_published', models.BooleanField(default=True)),
                ('reciept_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='plot',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.CASCADE, to='client_payments.Plot'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]