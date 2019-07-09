from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from .models import Tweet, User, Like, Comment
from django.views import generic

#投稿関連
# from django import forms
# from .forms import TweetForm
from . import forms
#現在時刻
from datetime import datetime

#ユーザー新規登録(ボツ)
from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from django.views.generic import CreateView, View
# from . forms import UserCreateForm

# ユーザー新規登録(new!!!)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy




def index(request):
  tweet_list = Tweet.objects.all()
  context = {
  'lists': tweet_list,
  }
  return render(request, 'pictweet/index.html', context)



def new(request):
# def new(forms.ModelForm): #投稿関連
  form = forms.TweetForm(request.GET or None)
  model = Tweet  #投稿関連
  fields = ('text', 'image')  #投稿関連
  if request.method == 'POST':
    Tweet.objects.create(
      text = Tweet.text,
      # image = Tweet.image,
      date_time = datetime.now()
      # user_id_id = request.user.id
      )
    return redirect(to="/pictweet")

    # if form.is_valid():
    #     tweet = Tweet()
    #     book.title = form.cleaned_data['title']
    #     book.author = form.cleaned_data['author']
    #     book.holder = form.cleaned_data['holder']
    #     book.user = form.cleaned_data['user']
    #     book.published_date = form.cleaned_data['published_date']
    #     book.purchased_date = form.cleaned_data['purchased_date']
    #     book.isbn = form.cleaned_data['isbn']
    #     book.comment = form.cleaned_data['comment']

    #     Book.objects.create(
    #         title=book.title,
    #         author=book.author,
    #         holder=book.holder,
    #         user=book.user,
    #         published_date=book.published_date,
    #         purchased_date=book.purchased_date,
    #         isbn=book.isbn,
    #         comment=book.comment,
    #     )
    #     return redirect('book:book_list')


  return render(request, 'pictweet/new.html', {'form': form})
  


def create(request):
  #仮置き
  if request.method == 'POST':
    msg = Tweet.objects.create(tweet=request.POST['word'])
    msg.save()
    return redirect(to="/pictweet")

  return render(request, 'pictweet/new.html')


def user(request):
  #仮置き
  tweet_list = Tweet.objects.all()
  # tweet_list = Tweet.objects.filter(user_id=user.id)
  context = {
  'lists': tweet_list,
  }
  return render(request, 'pictweet/index.html', context)
  # return render(request, 'pictweet/index.user', context)



class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "pictweet/login.html"

class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "pictweet/logout.html"

class createView(CreateView):
    form_class = UserCreationForm
    template_name = "pictweet/createuser.html"
    success_url = reverse_lazy("login")












# # # 新規登録(ボツ)
# # # class Create_Account(CreateView):
# # #     def post(self, request, *args, **kwargs):
# # #         form = UserCreateForm(data=request.POST)
# # #         if form.is_valid():
# # #             form.save()
# # #             フォームから'username'を読み取る
# # #             nickrname = form.cleaned_data.get('username')
# # #             email = form.cleaned_data.get('email')
# # #             フォームから'password'を読み取る
# # #             password = form.cleaned_data.get('password')
# # #             user = authenticate(nickname=nickname, email=email, password=password)
# # #             login(request, user)
# # #             return redirect('/')
# # #         return render(request, 'createuser.html', {'form': form,})

# # #     def get(self, request, *args, **kwargs):
# # #         form = UserCreateForm(request.POST)
# # #         return  render(request, 'createuser.html', {'form': form,})

# # # create_account = Create_Account.as_view()


# # # ログイン機能(ボツ)
# # # class Account_login(View):
# # #     def post(self, request, *arg, **kwargs):
# # #         form = LoginForm(data=request.POST)
# # #         if form.is_valid():
# # #             nickname = form.cleaned_data.get('nickname')
# # #             user = User.objects.get(nickname=nickname)
# # #             login(request, user)
# # #             return redirect('/')
# # #         return render(request, 'login.html', {'form': form,})

# # #     def get(self, request, *args, **kwargs):
# # #         form = LoginForm(request.POST)
# # #         return render(request, 'login.html', {'form': form,})

# # # account_login = Account_login.as_view()



