# Generated by Django 2.1.7 on 2019-05-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_stations', '0007_auto_20190526_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='main_image',
        ),
        migrations.AddField(
            model_name='station',
            name='additional_images',
            field=models.ManyToManyField(to='U_stations.image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(height_field=100, upload_to='static/img/', width_field=100),
        ),
    ]
