from django.db import models


class info_table(models.Model):
    username = models.CharField(max_length=20, blank=False, verbose_name = 'Имя пользователя')
    email = models.CharField(max_length=20, blank=False, verbose_name = 'Почта')
    number = models.CharField(max_length=11, verbose_name = 'Номер')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ['time_create', 'username']