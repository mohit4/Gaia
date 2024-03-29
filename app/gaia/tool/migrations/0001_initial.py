# Generated by Django 3.1 on 2021-05-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(help_text='E.g. To navigate, For Healing etc.', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='E.g. Iron Man Suit, Agni V, Plasma Gun etc.', max_length=50)),
                ('description', models.TextField(help_text='Some words about this weapons.')),
                ('abilities', models.ManyToManyField(related_name='weapons', to='tool.Ability')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='E.g. Navigator, Magic Wand, Inverter cell etc.', max_length=50)),
                ('description', models.TextField(help_text='Some words about this tool.')),
                ('abilities', models.ManyToManyField(related_name='tools', to='tool.Ability')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
