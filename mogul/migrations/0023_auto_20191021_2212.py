# Generated by Django 2.1.5 on 2019-10-21 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mogul', '0022_auto_20191021_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='flight',
        ),
        migrations.AlterUniqueTogether(
            name='route',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='route',
            name='airline',
        ),
        migrations.RemoveField(
            model_name='route',
            name='dest_airport',
        ),
        migrations.RemoveField(
            model_name='route',
            name='fleet',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]