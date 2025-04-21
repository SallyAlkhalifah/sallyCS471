from django.db import models
from django.utils import timezone
import datetime

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)

class Author(models.Model):
    name = models.CharField(max_length= 300)
    
class Book(models.Model):
     title = models.CharField(max_length = 50)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     rating = models.SmallIntegerField(default = 1)
     pubdate= models.DateTimeField(default=timezone.now)
     author = models.ManyToManyField(Author)
     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
     
     class Meta:
         ordering = ['title']

   