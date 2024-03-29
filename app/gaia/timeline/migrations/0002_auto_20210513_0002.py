# Generated by Django 3.1 on 2021-05-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='end_period',
            field=models.BigIntegerField(help_text='E.g. 1914, 2000, 420 etc.'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='start_period',
            field=models.BigIntegerField(help_text='E.g. 1914, 2000, 420 etc.'),
        ),
    ]
