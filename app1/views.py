from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *


def pageNotFound(request,exception):
    return HttpResponseNotFound('<h>Страницы не существует</h>')

def index(request):
    
    return render(request,'app1/index.html', {'title':'Главная страница'})

def about(request):
    return render(request, 'app1/about.html', {'title':'О нас',})

def users(request):
    posts = info_table.objects.all()
    return render(request,'app1/users.html', {'title':"Список пользователей", 'post':posts})
