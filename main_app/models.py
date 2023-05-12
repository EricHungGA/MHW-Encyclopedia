from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User

class Material_List_Item(models.Model):
    item = models.TextField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')
    
class Monster_Image(models.Model):
    name = models.CharField()
    image = models.CharField()

class Small_Monster_Image(models.Model):
    name = models.CharField()
    image = models.CharField()