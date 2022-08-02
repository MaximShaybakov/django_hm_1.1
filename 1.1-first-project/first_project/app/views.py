from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    msg = f'<h3> Текущее время: {datetime.datetime.now().time()} </h3>'
    return HttpResponse(msg)


def workdir_view(request):
    list_dir = os.listdir(path='.')
    msg = f" <h1>Cписок файлов в рабочей директории: </h1>{''.join(f'<h4>{item}</h4>' for item in list_dir)}"
    return HttpResponse(msg)
