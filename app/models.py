from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass
    

class Blog(models.Model):
    BL = "Blog"
    AN = "Annoucement"
    
    choose = (
        (BL, "Blog"),
        (AN, "Announcement")
    )
    
    title = models.CharField(max_length=200)
    category = models.CharField(choices=choose, max_length=20, default="Blog")
    body = models.TextField(max_length=5000)
    image = models.ImageField(null=True, blank=True, upload_to="")
    
    def __str__(self):
        return self.title
    
    