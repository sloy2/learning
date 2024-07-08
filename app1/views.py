from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h>Страницы не существует</h>')

def index(request):
    
    return render(request,'app1/index.html', {'title':'Главная страница'})

def about(request):
    return render(request, 'app1/about.html', {'title':'О нас',})

def users_page(request):
    info_list = info_table.objects.filter(published=True).order_by('id')     #     http://127.0.0.1:8000/users/

    search_query = request.GET.get('search_query')
    if search_query:
        info_list = info_list.filter(username__icontains=search_query)

    return render(request, 'app1/users.html', {'title':"Список пользователей", 'infos': info_list})
   