from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News

def index(request):
    value=10
    n1 = News('Новость 1', 'Текст 1','07.11.2023')
    n2 = News('Новость 2', 'Текст 2', '08.11.2023')
    l=[n1, n2]

    context = {'title':'Главная страница',
               'header1':'Заголовок страницы',
               #'value':value,
               'numbers':l,
               }
    #return HttpResponse('<h1> Ура, работает! </h1>')
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('<h1> О нас </h1>')

def contacts(request):
    return HttpResponse('<h1> Контакты </h1>')

def sidebar(request):
    return render(request, 'main/sidebar.html')