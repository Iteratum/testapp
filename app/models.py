from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class PostCategory(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(PostCategory, null=True, on_delete=models.CASCADE, related_name="type")
    body = models.TextField(max_length=5000)
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    
    def __str__(self):
        return self.title