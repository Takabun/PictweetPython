from django.urls import path

from . import views
#ログアウト
# from django.contrib.auth.views import logout

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('user/', views.user, name='user'),
    # path('logout/', logout, {'template_name': 'index.html'}, name='logout'), 
    # path('logout/', logout, {'template_name': 'index.html'}, name='logout'), 
    path('createuser/', views.Create_Account, name='createuser'),
    path('login/', views.Account_login, name='login'),
    path('logout/', views.index, name='logout'),
]