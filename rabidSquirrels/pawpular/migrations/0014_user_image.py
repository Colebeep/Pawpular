# Generated by Django 2.0.2 on 2018-03-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0013_auto_20180324_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]