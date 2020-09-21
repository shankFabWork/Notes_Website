from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    front=models.ImageField(default="front.jpg",upload_to='front_pics')
    back=models.ImageField(default="back.jpg",upload_to='back_pics')
    about=models.CharField(max_length=100)
    desc=models.TextField(blank=False)

    