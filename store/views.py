from django.shortcuts import render
from .models import Glasses, CustomerReviews


def index(request):
    glasses = Glasses.objects.all()
    reviews = CustomerReviews.objects.all()[len(CustomerReviews.objects.all()) - 3 : ]
    return render(request, 'store/index.html', {'glasses': glasses, 'reviews': reviews})


def shop(request):
    return render(request, 'store/shop.html')


def glasses(request):
    glasses = Glasses.objects.all()
    return render(request, 'store/glasses.html', {'glasses': glasses})


def contact(request):
    return render(request, 'store/contact.html')


def about(request):
    return render(request, 'store/about.html')


def login(request):
    return render(request, 'store/login.html')


def register(request):
    return render(request, 'store/register.html')
