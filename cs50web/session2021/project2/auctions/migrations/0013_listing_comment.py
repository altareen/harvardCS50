# Generated by Django 3.2 on 2021-05-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_listing_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='comment',
            field=models.ManyToManyField(blank=True, related_name='listings', to='auctions.Comment'),
        ),
    ]