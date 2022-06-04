from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=255)

 # The old way

    #mobile = models.CharField(max_length=10)
    # def __str__(self):
    #     return f'Owner ({ self.name})'

# Meta class for defining the meta, pre sorting
    class Meta:
        ordering = ['name']
# new Way

    def __str__(self) -> str:
        return self.name

class Number(models.Model):
    owner = models.ForeignKey(Owner,on_delete= models.CASCADE)
    code = models.CharField(max_length=2)
    mobile = models.CharField(max_length=10)
    def __str__(self):
        return f' +{ self.code} {self.mobile}'

class Vehicle(models.Model):
    owner = models.ForeignKey(Owner,on_delete= models.CASCADE)
    MOdel = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.MOdel}'



