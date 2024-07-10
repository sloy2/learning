from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AddForm
from django.urls import reverse_lazy
from django.db.models import Q


def index(request):
    return render(request,'app1/index.html', {'title':'Главная страница'})

def about(request):
    return render(request, 'app1/about.html', {'title':'О нас',})

class infoUsers(ListView):
    model=info_table
    template_name = 'app1/users.html'
    context_object_name = 'infos'
    extra_context ={'title':"Список пользователей"}

    def get_queryset(self):
        queryset = super().get_queryset().filter(published=True).order_by('id')
        search_query = self.request.GET.get('search_query')
        
        if search_query:
            queryset = queryset.filter(
                Q(username__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(number__icontains=search_query)
            )
            
        return queryset
    
class addUsers(CreateView):
    model = info_table
    form_class = AddForm
    template_name = 'app1/addpage.html'
    success_url = reverse_lazy('users_page')
    extra_context ={'title':"Добавление записи"}
    
class updateUsers(UpdateView):
    model = info_table
    form_class = AddForm

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({
            'success': True, 
            'data': {
                'username': self.object.username,
                'email': self.object.email,
                'number': self.object.number,
                'time_update': self.object.time_update.strftime('%Y-%m-%d %H:%M:%S'),
            }
        })

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'errors': form.errors})

class deleteUsers(DeleteView):
    model = info_table
    success_url = reverse_lazy('users_page') 

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return JsonResponse({'success': True})
    