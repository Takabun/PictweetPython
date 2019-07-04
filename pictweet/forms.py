from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

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


#新規登録
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['nickname'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    class Meta:
       model = User
       fields = ("nickname", "email", "password",)

#ログイン
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['nickname'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'
