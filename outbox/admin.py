from django.contrib import admin
from outbox.models import sendData
# Register your models here.
admin.site.register(sendData)