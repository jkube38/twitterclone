from django.db import models

from twitteruser.models import Tweeter
from tweet.models import Tweet


# Create your models here.
class Notifications(models.Model):
    tweeter = models.ForeignKey(Tweeter, on_delete=models.CASCADE)
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
