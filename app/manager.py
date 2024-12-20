#A custom manager is required to handle user creation (both regular users and superusers).

#Set the custom user model in the settings.py: You will have to point Django to your custom user model by adding AUTH_USER_MODEL in settings.py

from django.contrib.auth.models import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        email = self.lowercase_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        email = self.lowercase_email(email)
        return self._create_user(email, password, **extra_fields)


    @staticmethod
    def lowercase_email(email):
        """
        lowercase the email address so that when users log in we can match lowercase login details
        """
        email = email or ""
        try:
            email = email.strip().lower()
        except ValueError:
            pass
        return email