from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
        'Приветствие': reverse('hello')
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


def summator(request, a, b):
    val = int(a) + int(b)
    return HttpResponse(f'Result = {val}')


def hello(request):
    # name = request.GET['name']
    # age = request.GET['age']
    name = request.GET.get('name')
    age = int(request.GET.get('age', 0))
    return HttpResponse(f'Hello, {name}!\nYoure age is {age}.')


def welcome(request):
    page = 'app/some_page.html'
    context = {
        'count_people': 10,
        'donate': [1, 34, 56, 43],
        'hello': 'Hello, friends!'
    }
    return render(request, page, context)


CONTENT = [str(i) for i in range(10000)]

def show_list(request):
    path_to_html = 'app/pagi.html'
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    num_page = paginator.get_page(page_number)
    context = {
        'page': num_page
    }
    return render(request, path_to_html, context)