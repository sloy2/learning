from django.contrib import admin
from .models import *

class info_tableAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'number', 'time_create', 'published')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email')

admin.site.register(info_table, info_tableAdmin)    