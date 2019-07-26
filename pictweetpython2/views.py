from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tweet, User, Like, Comment
from django.views import generic
from . import forms
from datetime import datetime #現在時刻
from django.contrib.auth.models import User #(現在の)authユーザー
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView, FormView,ListView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from pure_pagination.mixins import PaginationMixin #ページネーション
from django.contrib.auth.decorators import login_required


class index(PaginationMixin, ListView):
    model = Tweet
    paginate_by = 5
    template_name = "pictweet/index.html"
    #クラスベースなので、"tweet =..."の形でorder_by('-date_time')を付与する事は出来ないため下記を定義。
    def get_queryset(self):
        return super().get_queryset().order_by('-date_time')


@login_required
def new(request):
    if request.method == 'POST':
        form = forms.TweetForm(request.POST, request.FILES) #アップロードされたファイルはrequest.FILESに入る
        if form.is_valid(): 
            form = form.save(commit=False)  #これをつけると、["tweet"is not defined]のエラーが無くなり、user_idをセットできるようになった
            form.user = request.user
            form.save()
            return redirect("pictweetpython2:index")
    else:
        form = forms.TweetForm()
    return render(request, 'pictweet/new.html', {'form': form})  #インデントがズレてると"No HTTP Method"エラー発生


def show(request, id=id):  #urls.py中で、path(pk)ではなくurl(id)で定義している
    tweet = get_object_or_404(Tweet, pk=id)
    comments = Comment.objects.filter(tweet_id=id)
    #↓コメント機能
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
    return render(request, 'pictweet/show.html', 
    {'tweet': tweet, 'comments': comments, 'form': form}) # {}1つの中に全ての要素を統合する


def edit(request, pk):  #urls.py中、url(id)で定義している
    tweet = get_object_or_404(Tweet, pk=pk)  # Tweetの、idではなくpkを指定する
    if request.method == 'POST':
        #↓引数、この順番でないとエラーがでる。
        form = forms.TweetForm(request.POST, request.FILES, instance=tweet) # instance =tweetが無かったら、user_idも追記する必要あり
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.save()
            return redirect('pictweetpython2:index')
    else:
        form = forms.TweetForm(instance=tweet) # こうする事で更新前の値が入ってくる！！
    return render(request, 'pictweet/edit.html',  {'form': form})


def delete(request, id=id):
    tweet = Tweet.objects.filter(id=id)
    tweet.delete()
    return render(request, "pictweet/delete.html")


class user(DetailView):
    model = User
    template_name = "pictweet/user.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_list = Tweet.objects.filter(user_id=self.kwargs['pk']) # pkを指定してデータを絞り込む
        context['tweets'] = data_list
        return context


class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "pictweet/login.html"


class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "pictweet/logout.html"


class createView(CreateView):
    form_class = UserCreationForm
    template_name = "pictweet/createuser.html"
    success_url = reverse_lazy("pictweetpython2:login")


@login_required
def like(request, **kwargs): #いいね機能
    tweet = Tweet.objects.get(id=kwargs['tweet_id'])
    is_like = Like.objects.filter(user=request.user).filter(tweet=tweet).count()
    # unlike
    if is_like > 0 :
        liking = Like.objects.get(tweet__id=kwargs['tweet_id'], user=request.user)
        liking.delete()
        tweet.like_count -= 1
        tweet.save()
        return redirect(reverse_lazy("pictweetpython2:index"))
    # like
    tweet.like_count += 1
    tweet.save()
    like = Like()
    like.user = request.user
    like.tweet = tweet
    like.save()
    return redirect(reverse_lazy("pictweetpython2:index"))


#index、関数ビューの時はこちらを記載。しかしpaginagte導入に際しclassベースへ修正。tweet=を定義でき、それをhtmlへ渡せる。
# def index(request):
#   tweets = Tweet.objects.all().order_by('-date_time')
#   paginate_by = 10
#   return render(request, 'pictweet/index.html', {'tweets': tweets})
