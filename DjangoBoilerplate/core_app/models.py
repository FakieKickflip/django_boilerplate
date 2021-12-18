from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.



def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='Deleted player')[0]





class Author(models.Model):
    name = models.CharField(max_length=40, blank=True, default='default_name')
    age = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, default=timezone.now) 
    updated_at = models.DateTimeField(blank=True, auto_now=True) #date, when the objects gets updated
   
    def __str__(self):
        return str(self.name) 


class Book(models.Model):
    title = models.CharField(max_length=240, blank=True, null=True) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=timezone.now) 
    updated_at = models.DateTimeField(blank=True, auto_now=True) #date, when the objects gets updated

    def __str__(self) -> str:
        return str(self.title)       