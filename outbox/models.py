from django.db import models

# Create your models here.
class sendData(models.Model):
    send_date=models.CharField(max_length=50)
    send_from=models.CharField(max_length=200)
    send_to=models.CharField(max_length=200)
    send_subject=models.CharField(max_length=200)
    send_body=models.CharField(max_length=500)
    def __str__(self):
        return self.send_subject