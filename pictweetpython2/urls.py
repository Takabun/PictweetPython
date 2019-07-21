from django.urls import path

from . import views
#ログアウト
# from django.contrib.auth.views import logout
app_name = 'pictweetpython2'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('new/', views.new, name='new'),
    path('user/', views.user, name='user'),
    path('login/', views.loginView.as_view(), name="login"),
    path('logout/', views.logoutView.as_view(), name="logout"),
    path('createuser/', views.createView.as_view(),name="create"), # 追記

]