from django.urls import path, include
from.import views

from eventsapp.views import  subscribe
urlpatterns=[
path('', views.home,name='home'),

path('blog', views.blog,name='blog'),

path('index', views.index,name='index'),
path('register', views.register,name='register'),

path('profile', views.profile,name='profile'),
path('login', views.login,name='login'),
path('event1', views.event1,name='event1'),
path('logout', views.logout,name='logout'),
path('sample', views.sample,name='sample'),

path('event2', views.event2,name='event2'),
path('event3', views.event3,name='event3'),
path('event4', views.event4,name='event4'),
path('resetpassword', views.resetpassword,name='resetpassword'),

    path('subscribe', subscribe, name='subscribe'),
    path('userpage', views.userpage, name='userpage'),
]