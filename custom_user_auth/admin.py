from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustUserAmdin(UserAdmin):
    ordering = ['phonenumber']


admin.site.register(User, CustUserAmdin)
