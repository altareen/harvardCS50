# Generated by Django 3.2.3 on 2021-06-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
