from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Clothe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.CharField(max_length=15)
    type = models.CharField(max_length=20)
    cover = models.ImageField()


    def __str__(self):
        return self.material



