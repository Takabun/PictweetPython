from django.urls import path
from django.conf.urls import url
from . import views
#ログアウト
# from django.contrib.auth.views import logout



app_name = 'pictweetpython2'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('new/', views.new, name='new'),
    path('user/<int:pk>/', views.user.as_view(), name='user'),
    url(r'^show/(?P<id>\d+)/$', views.show, name='show'), #urlでidを拾ってくパターン
    path('edit/<int:pk>/', views.edit, name='edit'), #pathでpkを拾ってくるパターン
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    path('login/', views.loginView.as_view(), name="login"),
    path('logout/', views.logoutView.as_view(), name="logout"),
    path('createuser/', views.createView.as_view(),name="create"),
    url(r'^(?P<tweet_id>[0-9]+)/like/$', views.like, name='like'),#いいね機能
]