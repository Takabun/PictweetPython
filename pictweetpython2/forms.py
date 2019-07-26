from django import forms
from .models import User
from django.contrib.auth import forms as auth_forms
from .models import Tweet, Comment #modelform導入につき


class TweetForm(forms.ModelForm):
    """投稿画面用のフォーム"""
    class Meta:
        model = Tweet
        fields = ('text', 'image')


class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'ユーザ名'}))
        fields = ('text',)