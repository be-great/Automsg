# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy


class AutoMsgUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class AutoMsgUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(unique=True)
    username = models.CharField(
        gettext_lazy("username"),
        max_length=150,
        unique=True,
        help_text=gettext_lazy(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": gettext_lazy("A user with that username already exists."),
        },
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', "last_name", 'username']
    objects = AutoMsgUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
