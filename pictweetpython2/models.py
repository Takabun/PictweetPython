from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings  #usersを修正するために記載
# Create your models here.

class User(models.Model):
  nickname = models.CharField(max_length=150)
  password = models.CharField(validators=[MinLengthValidator(6)],max_length=20)
  created_at = models.DateTimeField()


class Tweet(models.Model):
    """Tweetモデル"""
    class Meta:
        db_table = 'tweet'
    text = models.TextField(max_length=140, blank=False)
    image = models.ImageField(upload_to='documents/')
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)



class Comment(models.Model):
  class Meta:
    db_table = 'comment'
  text = models.TextField(max_length=140, blank=False)
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like_user')
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

