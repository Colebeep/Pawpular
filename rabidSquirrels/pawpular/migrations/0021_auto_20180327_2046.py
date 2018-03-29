# Generated by Django 2.0.3 on 2018-03-28 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0020_auto_20180327_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='feedPosts',
            field=models.ManyToManyField(blank=True, to='pawpular.FeedPost'),
        ),
        migrations.AddField(
            model_name='user',
            name='mapPosts',
            field=models.ManyToManyField(blank=True, to='pawpular.MapPost'),
        ),
        migrations.AddField(
            model_name='user',
            name='pets',
            field=models.ManyToManyField(blank=True, to='pawpular.Pet'),
        ),
        migrations.AddField(
            model_name='user',
            name='servicePosts',
            field=models.ManyToManyField(blank=True, to='pawpular.ServicePost'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pawpular.User'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pawpular.User'),
        ),
    ]