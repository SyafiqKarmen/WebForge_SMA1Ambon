from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect

# Sign-in page
def index(request):
    if request.method == "POST":
        return redirect('dashboard')
    return render(request, 'index.html')

# Dashboard page
def dashboard(request):
    return render(request, 'dashboard.html')

# Histori page
def histori(request):
    return render(request, 'histori.html')

# Logout
def logout_view(request):
    return redirect('signin')

# Help page
def help_page(request):
    return render(request, 'help.html')

# Izin page
def izin_page(request):
    return render(request, 'izin.html')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='signin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('histori/', histori, name='histori'),
    path('logout/', logout_view, name='logout'),
    path('help/', help_page, name='help'),
    path('izin/', izin_page, name='izin'),  
]
