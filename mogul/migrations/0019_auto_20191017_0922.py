# Generated by Django 2.1.5 on 2019-10-17 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mogul', '0018_auto_20191017_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('fleet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mogul.Aircraft')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mogul.Airline')),
            ],
            options={
                'db_table': 'fleet',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_no', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mogul.Airline')),
                ('dest_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mogul.Airport')),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mogul.Fleet')),
            ],
            options={
                'db_table': 'route',
            },
        ),
        migrations.AlterUniqueTogether(
            name='route',
            unique_together={('airline', 'flight_no')},
        ),
        migrations.AlterUniqueTogether(
            name='fleet',
            unique_together={('fleet_id', 'airline')},
        ),
    ]
