from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    is_master = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Master(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    image = models.ImageField(upload_to='master_images/')
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100, default=None)
    description = models.TextField()
    experience = models.IntegerField()
    
    def str(self):
        return self.user.name

class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='master')
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    description = models.TextField()