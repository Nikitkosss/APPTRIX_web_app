from django.shortcuts import render

from api.models import Coin, News


def index(request):
    news = News.objects.all()
    return render(request, 'posts/index.html', {'news': news})


def crypto(request):
    coins = Coin.objects.all()
    return render(request, 'crypto/crypto.html', {'coins': coins})
