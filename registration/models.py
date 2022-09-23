from django.db import models

# Create your models here.
class userData(models.Model):
    fullname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.fullname + " " + "(" + self.phone + ")"