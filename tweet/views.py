from django.shortcuts import render, redirect
import re
from django.contrib.auth.decorators import login_required

from tweet.models import Tweet
from tweet.forms import NewTweetForm
from twitteruser.models import Tweeter
from notification.models import Notifications


# Create your views here.
@login_required(login_url='/login/')
def create_tweet_view(request, username):
    user = Tweeter.objects.get(username=username)
    context = {}
    if request.method == 'POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body=data['body'],
                author=request.user
            )

            # Looks for a mention and creates a notification
            mention_search = data['body']
            mention_re = re.compile(r'(@[^\s,.:\'"!#$%^&*()]+)')
            post_search = mention_re.findall(mention_search)
            if post_search:
                mentioned = Tweeter.objects.filter(username=post_search[0][1:])
                mention_tweet = Tweet.objects.filter(body=data['body'])
                Notifications.objects.create(
                    tweeter=mentioned[0],
                    tweet_id=mention_tweet[0]
                )
            return redirect('home')

    # User Info for template
    user_tweets = Tweet.objects.filter(author=user)
    num_tweets = len(list(user_tweets))
    num_following = len(list(user.following.all()))
    form = NewTweetForm()
    context.update(
        {
            'form': form,
            'num_tweets': num_tweets,
            'num_following': num_following,
            'user': user
        })
    return render(request, 'tweet.html', context)
