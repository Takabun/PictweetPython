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
from django.views.generic import TemplateView,CreateView, FormView,ListView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
#ページネーション
from pure_pagination.mixins import PaginationMixin


#関数ビューの時はこっち。paginagte導入するまで。tweet=を定義でき、それをhtmlへ渡せる。
# def index(request):
#   tweets = Tweet.objects.all().order_by('-date_time')
#   paginate_by = 10
#   return render(request, 'pictweet/index.html', {'tweets': tweets})
  
class index(PaginationMixin, ListView):
    model = Tweet
    paginate_by = 5
    template_name = "pictweet/index.html"
    #クラスベースなので、"tweet =..."の形で、order_by('-date_time')を付与する事は出来ない。よって下記を定義。objectsとして使える。
    def get_queryset(self):
        return super().get_queryset().order_by('-date_time')


from django.contrib.auth.decorators import login_required
@login_required
def new(request):
    if request.method == 'POST':
        #↓アップロードされたファイルはrequest.FILESに入る
        form = forms.TweetForm(request.POST, request.FILES)
        if form.is_valid(): 
            form = form.save(commit=False)
            #↑これをつけると、["tweet"is not defined]のエラーが無くなり、user_idをセットできるようになった
            # form.user_id = request.user.id #←_id とする必要は無い！！
            form.user = request.user
            form.save()
            return redirect("pictweetpython2:index")
    else:
        form = forms.TweetForm()
    return render(request, 'pictweet/new.html', {'form': form})
    #↑インデントがズレてると、"No HTTP Method"エラー発生


# # ↓userをクラスではなく関数で作ってみるとこうなる(けど、引数が合わない！！！)
# def user(request, self, **kwargs):
#   tweet_list = Tweet.objects.filter(user_id=self.kwargs['pk'])
#   context = {
#   'lists': tweet_list,
#   }
#   return render(request, 'pictweet/user.html', context)


class user(DetailView):
    model = User
    template_name = "pictweet/user.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_list = Tweet.objects.filter(user_id=self.kwargs['pk']) # pkを指定してデータを絞り込む
        context['tweets'] = data_list
        return context

#urls.py中、path(pk)ではなくurl(id)で定義している
def show(request, id=id):
    tweet = get_object_or_404(Tweet, pk=id)
    # comments = get_object_or_404(Comment, tweet_id=id)
    comments = Comment.objects.filter(tweet_id=id)
    #ここからコメント機能
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tweet = tweet
            comment.user = request.user
            comment.save()
            return redirect('pictweetpython2:show', id=tweet.id)
    else:
        form = forms.CommentForm()
    # ↓{}は、1つの中に全ての要素をと統合する必要あり
    return render(request, 'pictweet/show.html', 
    {'tweet': tweet, 'comments': comments, 'form': form})

#urls.py中、url(id)で定義している
def edit(request, pk):
    # Tweetの、idではなくpcを指定するんだ！
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == 'POST':
        #↓引数、この順番でないとエラーがでる。
        # また、instance =tweetが無かったら、user_idも追記する必要あり
        form = forms.TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.save()
            return redirect('pictweetpython2:index')
    else:
        # こうする事で、自動で更新前の値が入ってくる！！
        form = forms.TweetForm(instance=tweet)
    return render(request, 'pictweet/edit.html',  {'form': form})


def delete(request, id=id):
    # tweet = get_object_or_404(Tweet, pk=id)
    tweet = Tweet.objects.filter(id=id)
    tweet.delete()
    return render(request, "pictweet/delete.html")



class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "pictweet/login.html"

class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "pictweet/logout.html"

class createView(CreateView):
    form_class = UserCreationForm
    template_name = "pictweet/createuser.html"
    success_url = reverse_lazy("pictweetpython2:login")


