from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bid(models.Model):
    price = models.FloatField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchaser")


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person")


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="individual")
    category = models.CharField(max_length=64)
    timestamp = models.DateTimeField()
    url = models.TextField()
    bids = models.ManyToManyField(Bid, blank=True, related_name="listings")
    watchlist = models.ManyToManyField(User, blank=True, related_name="listings")
    active = models.BooleanField(default=True)
    comments = models.ManyToManyField(Comment, blank=True, related_name="listings")



