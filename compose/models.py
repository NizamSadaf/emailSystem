from django.db import models

# Create your models here.
class buffer(models.Model):
    uid=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    sub=models.CharField(max_length=200)
    body=models.CharField(max_length=200)

    def __str__(self):
        return self.sub