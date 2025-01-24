from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class UserLoginForm2(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'autofocus': True}))
    
class UserCreationForm2(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Requerido. Ingresa tu nombre.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Requerido. Ingresa tu apellido.")
    email = forms.EmailField(max_length=254, required=True, help_text="Requerido. Ingresa una dirección de correo electrónico válida.")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = ['first_name', 'last_name', 'email', 'membership_number']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'membership_number': 'Número de socio',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'membership_number': forms.TextInput(attrs={'placeholder': 'Número de socio'}),
        }
