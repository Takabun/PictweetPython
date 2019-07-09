from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth import forms as auth_forms



class TweetForm(forms.Form):
    text = forms.CharField(
        max_length=140,
        required=True,
        # blank=False
    )
#↑TextFieldにするとエラー。現状、modelとは齟齬がある状態

    image = forms.ImageField(
    # upload_to='pictweet/images/'
    )

# date_time = models.DateTimeField()
# user_id = models.ForeignKey(User, on_delete=models.CASCADE)
# like_count = models.IntegerField(default=0)


class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label