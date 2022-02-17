from django.urls import path

from  .views import index, shop, glasses, contact, about

urlpatterns = [
    path('', index),
    path('shop/', shop),
    path('glasses/', glasses),
    path('contact/', contact),
    path('about/', about),
]