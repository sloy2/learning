from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import *
from django.views.generic import ListView, CreateView
from .forms import AddForm

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h>Страницы не существует</h>')

def addpage(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            try:
                info_table.objects.create(**form.cleaned_data)
                return redirect('users_page')
            except:
                form.add_error(None, 'Ошибка добавления записи')
        else:
            form = AddForm()
    return render(request,'app1/addpage.html', {'title':'Добавить запись'})

def index(request):
    return render(request,'app1/index.html', {'title':'Главная страница'})

def about(request):
    return render(request, 'app1/about.html', {'title':'О нас',})

class infoUsers(ListView):
    model=info_table
    template_name = 'app1/users.html'
    context_object_name = 'infos'
    extra_context ={'title':"Список пользователей"}

#class addUsers(CreateView):
 #   form_class = AddForm


#def users_page(request):
   # info_list = info_table.objects.filter(published=True).order_by('id')     #     http://127.0.0.1:8000/users/

    #search_query = request.GET.get('search_query')
   # if search_query:
   #     info_list = info_list.filter(username__icontains=search_query)

   # return render(request, 'app1/users.html', {'title':"Список пользователей", 'infos': info_list})
   