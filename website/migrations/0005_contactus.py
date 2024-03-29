# Generated by Django 4.2.1 on 2023-09-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_events_occured'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Enter your email address')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
