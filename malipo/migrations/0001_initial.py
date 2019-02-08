# Generated by Django 2.1.5 on 2019-01-26 09:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realtors', '0001_initial'),
        ('listings', '0001_initial'),
        ('catalog', '0011_auto_20190125_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Malipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plot_no', models.CharField(blank=True, max_length=200, null=True)),
                ('account_date', models.DateField(null=True)),
                ('reciept_no', models.CharField(blank=True, max_length=200, null=True)),
                ('bankreciept_date', models.DateField(blank=True, null=True)),
                ('bank', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_branch', models.CharField(blank=True, max_length=200, null=True)),
                ('mpesamessage', models.TextField(blank=True, null=True)),
                ('mpesa_code', models.CharField(max_length=50, null=True)),
                ('mpesaphone_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Amount', models.IntegerField(null=True)),
                ('Balance', models.IntegerField(null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='reciept_pics')),
                ('Buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Buyer')),
                ('Owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Previouspayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.CharField(help_text='please input current amount to make it available as previous payment in next account update', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='malipo',
            name='Previouspayment',
            field=models.ManyToManyField(help_text='select payment method', to='malipo.Previouspayment'),
        ),
        migrations.AddField(
            model_name='malipo',
            name='Realtor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor'),
        ),
        migrations.AddField(
            model_name='malipo',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing'),
        ),
        migrations.AddField(
            model_name='malipo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
