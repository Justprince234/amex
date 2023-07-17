from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from  django.conf import settings
from datetime import timedelta
from django.contrib.auth.validators import UnicodeUsernameValidator

import random

def return_date_time():
    now = timezone.now()
    return now + timedelta(days=1)

# Create your models here.
class UserManager(BaseUserManager):
    
    def _create_user(self,username, email, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError("Username must be set")
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields) 
        user.save(using=self._db)
        return user
    
def random_account():
    return str(random.randint(1000000000, 10000000000))

class User(AbstractBaseUser, PermissionsMixin):

    """Custom user class inheriting AbstractBaseUser class."""
    
    full_name = models.CharField(max_length=100)
    account_number = models.CharField(default=random_account, unique=True, max_length=200)
    username = models.CharField(max_length=150, validators=[UnicodeUsernameValidator, ],unique=True)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", ]

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_email(self):
        return self.email