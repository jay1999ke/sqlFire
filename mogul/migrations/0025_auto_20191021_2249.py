# Generated by Django 2.1.5 on 2019-10-21 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mogul', '0024_auto_20191021_2212'),
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
        migrations.DeleteModel(
            name='Passenger',
        ),
    ]