from django.urls import path
from . import views
from django.shortcuts import render

# Your existing izin view
def izin_page(request):
    return render(request, 'izin.html')

urlpatterns = [
    path('', views.signin_view, name='signin'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('histori/', views.histori_view, name='histori'),
    path('help/', views.help_view, name='help'),
    path('izin/', izin_page, name='izin'),
    path('logout/', views.logout_view, name='logout'),
]