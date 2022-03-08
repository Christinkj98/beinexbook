from django.db import models

# Create your models here.
class beinexbooks(models.Model):
    Bookname = models.CharField(max_length=240)
    Author = models.CharField(max_length=240)
    Description = models.CharField(max_length=240)
    Timestamp = models.CharField(max_length=240,default="0")

    def __str__(self):
        return self.Bookname
     
class beinexusers(models.Model):
    Name = models.CharField(max_length=240)
    Username = models.CharField(max_length=240)
    Password = models.CharField(max_length=240)
    Designation = models.CharField(max_length=240)
    