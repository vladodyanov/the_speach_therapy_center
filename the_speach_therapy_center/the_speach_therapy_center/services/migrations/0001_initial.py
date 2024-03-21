# Generated by Django 5.0.2 on 2024-03-21 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuestionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Your name:')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question_one', models.TextField(choices=[('A1', 'Never'), ('A2', 'Rarely'), ('A3', 'Occasionally'), ('A4', 'Frequently'), ('A5', 'Always')], verbose_name='How often do you experience difficulty pronouncing certain sounds?')),
                ('question_two', models.TextField(choices=[('A1', 'Never'), ('A2', 'Rarely'), ('A3', 'Occasionally'), ('A4', 'Frequently'), ('A5', 'Always')], verbose_name='Do you feel confident when speaking in public?')),
                ('question_three', models.TextField(choices=[('A1', 'Never'), ('A2', 'Rarely'), ('A3', 'Occasionally'), ('A4', 'Frequently'), ('A5', 'Always')], verbose_name='Have you noticed any changes in your voice quality or pitch recently?')),
                ('question_four', models.TextField(choices=[('A1', 'Never'), ('A2', 'Rarely'), ('A3', 'Occasionally'), ('A4', 'Frequently'), ('A5', 'Always')], verbose_name='Do you struggle with stuttering or stammering?')),
                ('question_five', models.TextField(choices=[('A1', 'Never'), ('A2', 'Rarely'), ('A3', 'Occasionally'), ('A4', 'Frequently'), ('A5', 'Always')], verbose_name='Have you ever had difficulty understanding or following conversations?')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]