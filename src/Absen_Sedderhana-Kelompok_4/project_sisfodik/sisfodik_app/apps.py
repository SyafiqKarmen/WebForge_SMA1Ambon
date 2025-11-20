# sisfodik_app/apps.py

from django.apps import AppConfig

# Class name must match the one used in settings.py
class SisfodikAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sisfodik_app'