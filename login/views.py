from django.views.generic import CreateView, FormView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

def membership_application_view(request):
    if request.method == 'POST':
        form = MembershipApplicationForm(request.POST)
        if form.is_valid():
            # Guardar la solicitud
            application = form.save()

            # Enviar email al solicitante
            send_mail(
                'Solicitud recibida - Club Privado',
                'Gracias por tu solicitud. Estamos verificando tus datos y te contactaremos pronto.',
                settings.DEFAULT_FROM_EMAIL,
                [application.email],
                fail_silently=False,
            )

            # Enviar email al administrador
            send_mail(
                'Nueva Solicitud de Membresía',
                f"Se ha recibido una nueva solicitud:\n\n"
                f"Nombre: {application.first_name} {application.last_name}\n"
                f"Email: {application.email}\n"
                f"Número de socio: {application.membership_number}\n",
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            # Redirigir a la página de confirmación
            return redirect('login:membership_application_confirmation')

    else:
        form = MembershipApplicationForm()

    return render(request, 'login/membership_application.html', {'form': form})


def membership_application_confirmation_view(request):
    return render(request, 'login/membership_confirmation.html')


class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    form_class = UserLoginForm2
    redirect_authenticated_user = True

    def get_success_url(self):
        # Redirige al home de la app socio
        return self.request.GET.get('next', reverse_lazy('socio:home'))

class CustomLogoutView(LogoutView):
    next_page = 'web:home'
    
class PasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'login/password_reset.html'
    email_template_name = 'login/password_reset_email.html'
    html_email_template_name = 'login/password_reset_email.html'  # Plantilla de correo en formato HTML
    subject_template_name = 'login/password_reset_subject.txt'
    success_message = "Te hemos enviado un correo con instrucciones para restablecer tu contraseña."
    success_url = reverse_lazy('login:password_reset_done')

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'login/password_reset_done.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'login/password_reset_confirm.html'
    success_url = reverse_lazy('login:password_reset_complete')

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'login/password_reset_complete.html'
