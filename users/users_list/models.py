from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserBasic(models.Model):
    first_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length = 264)
    email = models.EmailField(max_length = 264, unique = True)

    def __str__(self):
        return self.email


class UserProfileInfo(models.Model):
    # it's like extend from User but not exactly!

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic= models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
