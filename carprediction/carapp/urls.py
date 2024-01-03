from django.urls import path
from carapp.views import *
urlpatterns = [
    path('',wellcome,name='music'),
    path('signin',signin,name='signin'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('home',home,name='home'),
    path('predict_price',predict_price,name='predict_price'),
    path('members',members,name='members'),
]
