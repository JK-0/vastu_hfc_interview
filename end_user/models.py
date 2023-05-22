from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError("Users should have a Email")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True

        user.save()
        return user


class User(AbstractUser):

    email = models.EmailField(unique=True, null=False)
    employee_code = models.CharField(max_length=10, null=True, blank=True)
    department = models.CharField(max_length=10, null=True, blank=True)
    designation = models.CharField(max_length=10, null=True, blank=True)
    level = models.CharField(max_length=10, null=True, blank=True)
    branch = models.CharField(max_length=10, null=True, blank=True)

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    manager = UserManager()

    def __str__(self):
        return self.email
