# Generated by Django 5.0.2 on 2024-03-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='speachcenteruser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='speachcenteruser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]