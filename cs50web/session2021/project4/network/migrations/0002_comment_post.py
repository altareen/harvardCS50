# Generated by Django 3.2.3 on 2021-06-08 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('likes', models.IntegerField()),
                ('comments', models.ManyToManyField(blank=True, related_name='listings', to='network.Comment')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individual', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]