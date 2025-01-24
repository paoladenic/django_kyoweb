from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

class MembershipApplication(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    membership_number = models.CharField(max_length=20, unique=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.membership_number}"

    def create_user(self):
        """Crea un usuario en el modelo User si no existe ya."""
        if not User.objects.filter(email=self.email).exists():
            password = User.objects.make_random_password()  # Generar contraseña aleatoria
            user = User.objects.create_user(
                username=self.email,
                email=self.email,
                first_name=self.first_name,
                last_name=self.last_name,
                password=password
            )
            # Notificar al usuario por correo
            self.notify_user(user, password)
            return user
        return None

    def notify_user(self, user, password):
        """Envía un correo al usuario con las credenciales iniciales."""
        send_mail(
            'Acceso Aprobado - #SOMOSKYO',
            f"Tu solicitud ha sido aprobada. Puedes iniciar sesión con:\n\n"
            f"Usuario: {user.email}\n"
            f"Contraseña: {password}\n\n"
            f"Por favor, cámbiala al iniciar sesión.",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

    def save(self, *args, **kwargs):
        """Sobrescribe el método save para crear el usuario automáticamente si es aprobado."""
        # Si la membresía es aprobada y el usuario no existe, crear usuario
        if self.is_approved:
            self.create_user()
        super().save(*args, **kwargs)
