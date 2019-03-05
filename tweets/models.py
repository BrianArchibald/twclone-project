from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    tweet_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date posted')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet_text

class Comment(models.Model):
    comment_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date posted')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment_text

class Message(models.Model):
    message = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date sent')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received")
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    read = models.BooleanField()

    def __str__(self):
        return self.message