# Generated by Django 4.2.4 on 2023-08-28 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['-eventDate'], 'verbose_name_plural': 'Events'},
        ),
    ]
