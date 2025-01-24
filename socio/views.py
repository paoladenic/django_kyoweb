from django.views.generic import UpdateView
from django.contrib.auth.views import PasswordChangeView, LogoutView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'socio/index.html')

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User 
    template_name = 'socio/edit_profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('socio:edit_profile_done')

    def form_valid(self, form):
        messages.success(self.request, "Perfil actualizado correctamente.")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'socio/change_password.html'
    success_url = reverse_lazy('socio:password_change_done')

    def form_valid(self, form):
        messages.success(self.request, "Tu contraseña ha sido cambiada exitosamente.")
        return super().form_valid(form)
    