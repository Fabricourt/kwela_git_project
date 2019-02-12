# Generated by Django 2.1.5 on 2019-01-20 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='realtor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor'),
        ),
    ]