import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'Andy'
email = 'andyalcivar@gmail.com'
password = 'domingo9'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superusuario '{username}' creado exitosamente.")
else:
    print(f"El usuario '{username}' ya existe.")