# Generated by Django 2.1.5 on 2019-02-03 10:21

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0002_auto_20190127_1326'),
        ('catalog', '0011_auto_20190125_1401'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('malipo', '0006_malipo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Malipo_two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plot_no', models.CharField(blank=True, max_length=200, null=True)),
                ('account_date', models.DateField(null=True)),
                ('reciept_no', models.CharField(blank=True, max_length=200, null=True)),
                ('bankreciept_date', models.DateField(blank=True, null=True)),
                ('bank', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_branch', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_agent_no', models.CharField(blank=True, max_length=200, null=True)),
                ('Amount', models.IntegerField(null=True)),
                ('Balance', models.IntegerField(null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='reciept_pics')),
                ('Buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Buyer')),
                ('Owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Owner')),
                ('Realtor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='malipo',
            name='mpesa_code',
        ),
        migrations.RemoveField(
            model_name='malipo',
            name='mpesamessage',
        ),
        migrations.RemoveField(
            model_name='malipo',
            name='mpesaphone_no',
        ),
        migrations.AddField(
            model_name='malipo',
            name='bank_agent_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
