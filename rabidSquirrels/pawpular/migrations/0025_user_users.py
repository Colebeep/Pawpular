# Generated by Django 2.0.2 on 2018-04-05 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pawpular', '0024_auto_20180327_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='users',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]