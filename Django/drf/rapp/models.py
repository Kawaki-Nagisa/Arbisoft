from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.

    This model replaces the default username field with an email field for user authentication.
    It also includes an optional date of birth field.

    Attributes:
        email (EmailField): The unique email address used for authentication.
        date_of_birth (DateField): The user's date of birth (optional).

    Inherits from:
        AbstractUser: Django's built-in user model class.

    """
    username = None
    email = models.EmailField(_("email address"), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        """
        Return the user's email address as the string representation of the user.

        Returns:
            str: The email address of the user.
        """
        return self.email
