from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from .models import Tweet, User, Like, Comment
from django.views import generic

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
from django.views.generic import TemplateView,CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
  tweets = Tweet.objects.all()
  return render(request, 'pictweet/index.html', {'tweets': tweets})

from django.contrib.auth.decorators import login_required
@login_required
def new(request):
    if request.method == 'POST':
        form = forms.TweetForm(request.POST, request.FILES)
        if form.is_valid(): 
            form = form.save(commit=False)
            #↑これをつけると、["tweet"is not defined]のエラーが無くなり、user_idをセットできるようになった
            form.user_id = request.user.id
            form.user_id = request.user.id
            form.save()
            return redirect("pictweet:index")
    else:
        form = forms.TweetForm()
    return render(request, 'pictweet/new.html', {'form': form})
    #↑インデントがズレてると、"No HTTP Method"エラー発生



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

