from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ContactForm

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def home(request):
    return render(request, 'web/index.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_body = render_to_string('web/contacto_email.html', {'name': name, 'email': email, 'message': message})

            subject = 'Nuevo mensaje de contacto'
            from_email = 'asociacion.kio@gmail.com'
            to_email = [email, 'asociacion.kio@gmail.com']

            email_message = EmailMultiAlternatives(subject, strip_tags(email_body), from_email, to_email)
            email_message.attach_alternative(email_body, "text/html")
            try:
                email_message.send()
                messages.success(request, '¡Mensaje enviado con éxito!')
                return redirect(reverse('web:home') + '#contacto')
            except Exception as e:
                print(f"Error al enviar el correo: {e}")  # Para debug
                messages.error(request, f'Error al enviar el correo: {e}')
                return redirect(reverse('web:home') + '#contacto')

        else:
            print("Errores del formulario:", form.errors)  # Añadido
            messages.error(request, 'Hubo un error en el formulario. Por favor, corrige los errores e intenta de nuevo.')
            return redirect(reverse('web:home') + '#contacto')
    else:
        form = ContactForm()

    return render(request, 'web/index.html', {'form': form})

def membresia(request):
    return render(request, 'web/membership.html')