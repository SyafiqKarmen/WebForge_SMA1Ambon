from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    KELAS_CHOICES = [
        ('X-1', 'X-1'),
        ('X-2', 'X-2'),
        ('X-3', 'X-3'),
        ('X-4', 'X-4'),
        ('X-5', 'X-5'),
        ('X-6', 'X-6'),
        ('X-7', 'X-7'),
        ('X-8', 'X-8'),
        ('X-9', 'X-9'),
        ('X-10', 'X-10'),
        ('XI-1', 'XI-1'),
        ('XI-2', 'XI-2'),
        ('XI-3', 'XI-3'),
        ('XI-4', 'XI-4'),
        ('XI-5', 'XI-5'),
        ('XI-6', 'XI-6'),
        ('XI-7', 'XI-7'),
        ('XI-8', 'XI-8'),
        ('XI-9', 'XI-9'),
        ('XI-10', 'XI-10'),
        ('XII-1', 'XII-1'),
        ('XII-2', 'XII-2'),
        ('XII-3', 'XII-3'),
        ('XII-4', 'XII-4'),
        ('XII-5', 'XII-5'),
        ('XII-6', 'XII-6'),
        ('XII-7', 'XII-7'),
        ('XII-8', 'XII-8'),
        ('XII-9', 'XII-9'),
        ('XII-10', 'XII-10'),
    ]
    
    kelas = models.CharField(max_length=10, choices=KELAS_CHOICES, blank=True, null=True)
    lokasi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.kelas or 'No Class'}"