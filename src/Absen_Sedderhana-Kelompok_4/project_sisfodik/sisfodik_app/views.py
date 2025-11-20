from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Update user location if provided
            if latitude and longitude:
                user.lokasi = f"Lokasi: {latitude}, {longitude}"
                user.save()
            return redirect('dashboard')
        else:
            return render(request, 'signin.html', {
                'error': 'Login gagal. Periksa username dan password.'
            })
    
    return render(request, 'signin.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {
        'username': request.user.username,
        'kelas': request.user.kelas,
        'lokasi': request.user.lokasi or "Lokasi tidak terdeteksi"
    })

@login_required
def help_view(request):
    return render(request, 'help.html', {
        'username': request.user.username,
        'kelas': request.user.kelas,
        'lokasi': request.user.lokasi or "Lokasi tidak terdeteksi"
    })