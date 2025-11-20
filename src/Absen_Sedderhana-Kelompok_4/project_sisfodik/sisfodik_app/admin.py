from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'kelas', 'lokasi', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informasi Tambahan', {'fields': ('kelas', 'lokasi')}),
    )