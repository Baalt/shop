from django.shortcuts import render


def index(request):
    return render(request, 'store/index.html')


def shop(request):
    return render(request, 'store/shop.html')


def glasses(request):
    return render(request, 'store/glasses.html')


def contact(request):
    return render(request, 'store/contact.html')


def about(request):
    return render(request, 'store/about.html')


def login(request):
    return render(request, 'store/login.html')


def register(request):
    return render(request, 'store/register.html')
