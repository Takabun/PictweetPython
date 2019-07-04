from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class User(models.Model):
  nickname = models.CharField(max_length=150)
  email = models.EmailField(unique=True)
  password = models.CharField(validators=[MinLengthValidator(6)],max_length=20)
  created_at = models.DateTimeField()


class Tweet(models.Model):
  text = models.TextField(max_length=140, blank=False)
  image = models.ImageField(upload_to='pictweet/images/', default='defo')
  date_time = models.DateTimeField()
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  like_count = models.IntegerField(default=0)



class Comment(models.Model):
  text = models.TextField(max_length=140, blank=False)
  tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField()


class Like(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
  post_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
  created_at = models.DateTimeField()

