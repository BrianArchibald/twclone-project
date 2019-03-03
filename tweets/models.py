from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    tweet_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date posted')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet_text
