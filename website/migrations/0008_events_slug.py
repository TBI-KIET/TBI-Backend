# Generated by Django 4.2.4 on 2023-10-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_events_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]
