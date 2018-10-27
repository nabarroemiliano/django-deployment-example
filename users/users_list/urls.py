from django.conf.urls import url
from users_list import views

app_name = 'users_list'

urlpatterns = [

    url(r'^users/$', views.users, name = 'users'),
    url(r'^formpage/$', views.form_user_view, name='form_name'),
    url(r'^registration/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
