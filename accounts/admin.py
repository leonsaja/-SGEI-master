from django.contrib import admin
from .models import User

# class Userform(admin.filters)
admin.site.register(User)
# Register your models here.
