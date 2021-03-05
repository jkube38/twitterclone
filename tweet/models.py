from django.db import models
from twitteruser.models import Tweeter
from django.utils import timezone


# Create your models here.
class Tweet(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(
            Tweeter,
            related_name='tweet_author',
            on_delete=models.CASCADE
            )
    submit_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
