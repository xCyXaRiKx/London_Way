# Generated by Django 2.1.7 on 2019-05-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_stations', '0011_auto_20190526_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='change_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]