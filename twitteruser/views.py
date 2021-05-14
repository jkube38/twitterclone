from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from twitteruser.models import Tweeter
from tweet.models import Tweet
from notification.models import Notifications
from twitteruser.forms import SignupForm


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


# Allows user to follow other users
def follow_view(request, username):
    follow_user = Tweeter.objects.get(username=username)
    user = request.user
    user.following.add(follow_user)
    user.save()
    return redirect('profile', follow_user)


# Allows user to unfollow other users
def unfollow_view(request, username):
    unfollow_user = Tweeter.objects.get(username=username)
    user = request.user
    user.following.remove(unfollow_user)
    user.save()
    return redirect('profile', unfollow_user)


@login_required(login_url='/login/')
def home_view(request):

    context = {}
    user = request.user
    num_following = len(list(user.following.all()))
    if num_following > 0:
        num_following = num_following - 1

    # Cleans up Notifications
    clean_mentions = Notifications.objects.filter(tweeter=request.user)
    for mention in clean_mentions:
        if mention.viewed:
            mention.delete()

    tweets = len(list(Tweet.objects.filter(author=user)))

    # sort tweets by who the user is following
    following_tweets = []
    all_tweets = Tweet.objects.all()
    following = user.following.all()
    for follow in following:
        for tweet in all_tweets:
            if follow == tweet.author:
                following_tweets.append(tweet)

    def time(x):
        return x.submit_time
    follow_tweets = sorted(following_tweets, key=time, reverse=True)

    # Gets Notifications for the user
    mentions = len(list(Notifications.objects.filter(tweeter=user)))
    context.update({
            'user': user,
            'tweets': tweets,
            'num_following': num_following,
            'follow_tweets': follow_tweets,
            'mentions': mentions
    })
    return render(
        request, 'home.html', context)


# Profile view
def profile_view(request, username):

    if request.user.is_authenticated:
        user = Tweeter.objects.get(username=username)
        user_tweets = Tweet.objects.filter(author=user)
        # sorts tweets by time
        u_tweets = []
        for tweet in user_tweets:
            u_tweets.append(tweet)

        def by_time(x):
            return x.submit_time

        sorted_tweets = sorted(u_tweets, key=by_time, reverse=True)
        num_tweets = len(list(user_tweets))
        num_following = len(list(user.following.all()))

        if num_following > 0:
            num_following = num_following - 1

        logged_in_user = request.user
        follow_list = logged_in_user.following.all()
        follow = user
        return render(
            request,
            'profile.html',
            {
                'user': user,
                'sorted_tweets': sorted_tweets,
                'num_tweets': num_tweets,
                'num_following': num_following,
                'follow': follow,
                'follow_list': follow_list
            })
    else:
        user = Tweeter.objects.get(username=username)
        user_tweets = Tweet.objects.filter(author=user)
        # sorts tweets by time
        u_tweets = []
        for tweet in user_tweets:
            u_tweets.append(tweet)

        def by_time(x):
            return x.submit_time

        sorted_tweets = sorted(u_tweets, key=by_time, reverse=True)
        num_tweets = len(list(user_tweets))

        num_following = len(list(user.following.all()))
        if num_following > 0:
            num_following = num_following - 1

        return render(
            request,
            'profile.html',
            {
                'user': user,
                'sorted_tweets': sorted_tweets,
                'num_tweets': num_tweets,
                'num_following': num_following,
            })


# Signup View
def signup_view(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweeter.objects.create(
                username=data['username'],
                email=data['email'],
            )
            new_user = Tweeter.objects.get(username=data['username'])
            print(new_user, 'pass:', data['password'])
            new_user.set_password(data['password'])
            new_user.following.add(new_user)
            new_user.save()
            return redirect('login')
    form = SignupForm()
    context.update({'form': form})
    return render(request, 'signup.html', context)


def tweet_view(request, post_id):
    tweet_id = Tweet.objects.get(id=post_id)
    return render(request, 'tweetpage.html', {'tweet_id': tweet_id})
