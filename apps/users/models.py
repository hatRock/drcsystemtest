from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Model for user profile details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=120)
    mobile = models.CharField(max_length=12)
    primary_email = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.user.username
