from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    # Custom user model manager where email is the unique identifiers
    # for authentication instead of usernames.

    def create_user(self, email, password, **extra_fields):

        # Create and save a User with the given email and password.

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        # Create and save a SuperUser with the given email and password.

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    # By default, the unique identifier of each user
    # is the username, this sets it to email instead
    USERNAME_FIELD = 'email'

    # This takes away the default required fields,
    # Now the only required fields are the unique identifier (email)
    # and password
    REQUIRED_FIELDS = []

    # Specifies model to use custom manager
    objects = CustomUserManager()
