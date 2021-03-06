# Generated by Django 3.2.7 on 2021-09-06 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservationApp', '0002_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservationApp.room', to_field='room_number'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
