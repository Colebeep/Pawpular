# Generated by Django 2.0.2 on 2018-03-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0017_mappost_imageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mappost',
            name='imageurl',
        ),
        migrations.AddField(
            model_name='mappost',
            name='imageUrl',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
