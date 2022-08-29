from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    phone = models.CharField(max_length=11,blank=True,null=True)
    token = models.CharField(max_length=10,blank=True,null=True)


class Profile(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.PROTECT)
    username = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.phone