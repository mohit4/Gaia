# Generated by Django 3.1 on 2021-05-13 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]