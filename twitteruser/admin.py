from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import Tweeter


# Register your models here.
UserAdmin.fieldsets += ('Tweet_Stats', {'fields': ('following', 'num_tweets')}),
admin.site.register(Tweeter, UserAdmin)
