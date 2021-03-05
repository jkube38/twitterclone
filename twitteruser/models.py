from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Tweeter(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False)
    num_tweets = models.IntegerField(default=0)

    def __str__(self):
        return self.username
