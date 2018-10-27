from django.contrib import admin
from users_list.models import User, UserProfileInfo

# Register your models here.
admin.site.unregister(User) #First unregister the old class
admin.site.register(User)
admin.site.register(UserProfileInfo)
