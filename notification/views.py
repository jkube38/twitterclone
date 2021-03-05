from django.shortcuts import render

from notification.models import Notifications
from tweet.models import Tweet


# Create your views here.
def notifications_view(request):
    # renders Notifications True to be deleted on home view
    user = request.user
    user_notifications = Notifications.objects.filter(tweeter=user)
    for notification in user_notifications:
        notification.viewed = True
        notification.save()
    # user Info for template
    user_tweets = Tweet.objects.filter(author=user)
    num_tweets = len(list(user_tweets))
    print(num_tweets)
    num_following = len(list(user.following.all()))

    author_link = user_notifications[0].tweet_id.author

    return render(
        request,
        'notifications.html',
        {
            'user_notifications': user_notifications,
            'num_tweets': num_tweets,
            'num_following': num_following,
            'author_link': author_link
        })
