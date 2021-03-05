# Generated by Django 3.1.7 on 2021-03-05 08:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweeter',
            name='following',
            field=models.ManyToManyField(default='self', to=settings.AUTH_USER_MODEL),
        ),
    ]
