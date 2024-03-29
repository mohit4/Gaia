# Generated by Django 3.1 on 2021-05-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20210514_0341'),
        ('character', '0002_auto_20210514_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='characters_associated', to='place.Event'),
        ),
    ]
