# Generated by Django 2.1.5 on 2019-01-20 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0001_initial'),
        ('catalog', '0002_auto_20190120_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='listing',
            field=models.ForeignKey(help_text='particular listing assigned', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing'),
        ),
        migrations.AddField(
            model_name='owner',
            name='realtor',
            field=models.ForeignKey(help_text='realtor assigned', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor'),
        ),
        migrations.AddField(
            model_name='property',
            name='realtor',
            field=models.ForeignKey(help_text='realtor assigned', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor'),
        ),
    ]