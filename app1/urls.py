from django.urls import path
from .views import *


urlpatterns = [
    path('main/',index) ,                        #     http://127.0.0.1:8000/main/
    path('users/', users)        #     http://127.0.0.1:8000/main/users/1/
]

