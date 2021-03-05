"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views
from authentication.views import login_view
from tweet.views import create_tweet_view
from notification.views import notifications_view

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('follow/<str:username>/', views.follow_view, name='follow'),
    path('unfollow/<str:username>/', views.unfollow_view, name='unfollow'),
    path('tweeter/<str:username>/', views.profile_view, name='profile'),
    path('tweet/<str:username>/', create_tweet_view, name='tweet'),
    path('notifications/', notifications_view, name='notifications'),
    path('signup/', views.signup_view, name='signup'),
    path('tweetdeets/<int:post_id>/', views.tweet_view, name='tweet2'),
    path('admin/', admin.site.urls),
]
