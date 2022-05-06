from django.contrib import admin

# Register your models here.
from .models import User, Bid, Comment, Listing

# Register your models here.
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Listing)
