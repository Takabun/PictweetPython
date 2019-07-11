from django.urls import path

from . import views
#ログアウト
# from django.contrib.auth.views import logout
app_name = 'pictweet'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('user/', views.user, name='user'),
    # path('logout/', logout, {'template_name': 'index.html'}, name='logout'), 
    # path('logout/', logout, {'template_name': 'index.html'}, name='logout'), 
    path('login/', views.loginView.as_view(), name="login"),
    path('logout/', views.logoutView.as_view(), name="logout"),
    path('createuser/', views.createView.as_view(),name="create"), # 追記

]