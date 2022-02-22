from django.urls import path

from  .views import *

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('glasses/', glasses, name='glasses'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]