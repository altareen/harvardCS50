from django.contrib import admin
from .models import User, Department, Course

# Register your models here.
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Course)

