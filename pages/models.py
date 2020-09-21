from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
