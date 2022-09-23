"""email_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('compose/',views.compose,name="compose"),
    path('get_email_info/',views.get_email_info,name="get_email_info"),
    path('get_email_info_compose/',views.get_email_info_compose,name="get_email_info_compose"),
    path('edit/',views.edit, name="edit"),
    path('edit-compose/',views.edit_compose, name="edit-compose"),
    path('start/',views.start, name="start"),
    path('start-compose/',views.start_compose, name="start-compose"),
]
