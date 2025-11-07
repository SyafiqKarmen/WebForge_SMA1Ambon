from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def tentang(request):
    return HttpResponse('Halaman Tentang')

def index(request):
    return HttpResponse('Hello World!!!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tentang/', tentang),
    path('index', index),
    path('', index),  # <--- ini buat route utama (localhost:8000/)
]
