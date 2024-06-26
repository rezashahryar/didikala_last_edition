from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validate_digit

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, validators=[validate_digit])
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'mobile']


class ActivationViaEmail(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=5)
    email = models.EmailField()
