# Generated by Django 5.0.2 on 2024-04-04 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_panel', '0007_treatmentplan_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatmentplan',
            name='user',
        ),
    ]
