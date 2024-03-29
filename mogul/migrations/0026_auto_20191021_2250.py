# Generated by Django 2.1.5 on 2019-10-21 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mogul', '0025_auto_20191021_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mogul.Customer')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mogul.Route')),
            ],
            options={
                'db_table': 'passenger',
            },
        ),
        migrations.AlterUniqueTogether(
            name='passenger',
            unique_together={('flight', 'seat_no')},
        ),
    ]
