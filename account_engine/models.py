from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE_CHOICES = [
    (False, 'Individual'),
    (True, 'Agent'),
]
class User(AbstractUser):
    mobile_number = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    user_type = models.BooleanField(choices=USER_TYPE_CHOICES)


    def __str__(self):
        return self.username
