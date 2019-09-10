# Generated by Django 2.1.5 on 2019-09-09 15:20

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone1', models.CharField(blank=True, max_length=100, null=True)),
                ('phone2', models.CharField(blank=True, max_length=100, null=True)),
                ('about_snippet', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('reload', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='header_carousel_pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('home_header', models.ImageField(blank=True, null=True, upload_to='home_header/')),
                ('home_header_statement1', models.CharField(blank=True, max_length=200, null=True)),
                ('home_header_statement2', models.CharField(blank=True, max_length=200, null=True)),
                ('home_header_statement3', models.CharField(blank=True, max_length=300, null=True)),
                ('home_header_1', models.ImageField(blank=True, null=True, upload_to='home_header/')),
                ('home_header_1_statement1', models.CharField(blank=True, max_length=200, null=True)),
                ('home_header_1_statement2', models.CharField(blank=True, max_length=200, null=True)),
                ('home_header_1_statement3', models.CharField(blank=True, max_length=300, null=True)),
                ('home_header_2', models.ImageField(blank=True, null=True, upload_to='home_header/')),
                ('home_header_2_statement1', models.CharField(blank=True, max_length=200, null=True)),
                ('home_header_2_statement2', models.CharField(blank=True, max_length=200, null=True)),
                ('home_header_2_statement3', models.CharField(blank=True, max_length=300, null=True)),
                ('reload', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/')),
                ('title', models.CharField(max_length=100)),
                ('statement', models.CharField(blank=True, max_length=100, null=True)),
                ('reload', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]