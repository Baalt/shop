from django.urls import path

from  .views import index, shop, glasses, contact, about

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('glasses/', glasses, name='glasses'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]