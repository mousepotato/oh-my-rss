from django.shortcuts import render
from .models import *


def index(request):
    """
    index home page
    :param request:
    :return:
    """
    # TODO 适配用户订阅参数
    articles = Article.objects.filter(status='active').order_by('-id')[:10]

    context = dict()
    context['articles'] = articles

    return render(request, 'index.html', context)


