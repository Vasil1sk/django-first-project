import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime
from django.http import JsonResponse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse("workdir")
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    reverse("time")
    return HttpResponse(f'Текущее время: {datetime.now().time()}')


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    reverse("workdir")
    directory = os.getcwd()
    files = os.listdir(directory)
    return JsonResponse({'Содержимое текущей директории': files}, json_dumps_params={'ensure_ascii': False, 'indent': 2}, safe=False)
    raise NotImplemented
