# Generated by Django 2.0.2 on 2018-03-27 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0015_auto_20180326_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='mappost',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='servicepost',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]