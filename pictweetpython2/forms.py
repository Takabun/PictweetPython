from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth import forms as auth_forms
from .models import Tweet #modelform導入につき


class TweetForm(forms.ModelForm):
    """投稿画面用のフォーム"""
    class Meta:
        #利用するモデルクラスを設定
        model = Tweet
        #利用するモデルのフィールドを設定
        fields = ('text', 'image')

# date_time = models.DateTimeField()
# user_id = models.ForeignKey(User, on_delete=models.CASCADE)
# like_count = models.IntegerField(default=0)


class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
