from django.db import models

# Create your models here.
class emailData(models.Model):
    email_date=models.CharField(max_length=50)
    email_from=models.CharField(max_length=200)
    email_to=models.CharField(max_length=200)
    email_subject=models.CharField(max_length=200)
    email_body=models.CharField(max_length=500)
    def __str__(self):
        return self.email_subject