from django.db import models


class info_table(models.Model):
    username = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=20, blank=False)
    number = models.CharField(max_length=11)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.username