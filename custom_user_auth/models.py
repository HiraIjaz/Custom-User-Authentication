from typing import Any, Optional
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, phonenumber, password, **extra_fields):
        if not phonenumber:
            raise ValueError('Phone number is required')

        user = self.model(phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, phonenumber, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(phonenumber, password, **extra_fields)

    def create_superuser(self, phonenumber, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(phonenumber, password, **extra_fields)


class User(AbstractUser):
    username = None
    phonenumber = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=50, default='Jane Doe')

    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['phonenumber']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0]
