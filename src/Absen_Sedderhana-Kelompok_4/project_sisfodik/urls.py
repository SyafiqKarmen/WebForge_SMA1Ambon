from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # render template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]