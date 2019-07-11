from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings  #usersを修正するために記載
# Create your models here.

class User(models.Model):
  nickname = models.CharField(max_length=150)
  password = models.CharField(validators=[MinLengthValidator(6)],max_length=20)
  created_at = models.DateTimeField()


class Tweet(models.Model):

  # # text = models.TextField(max_length=140, blank=False)
  # # image = models.ImageField(upload_to='pictweet/images/')
  # # date_time = models.DateTimeField()
  # # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  # # #↑元はUserのみだった
  # # like_count = models.IntegerField(default=0)
    """Tweetモデル"""
    class Meta:
        db_table = 'tweet' # データを保存するテーブル名
    text = models.TextField(max_length=140, blank=False)
    image = models.ImageField(upload_to='documents/')
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #↑元はUserのみだった
    like_count = models.IntegerField(default=0)



class Comment(models.Model):
  text = models.TextField(max_length=140, blank=False)
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField()


class Like(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
  created_at = models.DateTimeField()

