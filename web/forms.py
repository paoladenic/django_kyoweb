from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    # captcha = forms.CharField(required=False)
    
    if not settings.DEBUG:  # En producción usa reCAPTCHA
        captcha = ReCaptchaField(required=True)
    else:  # En desarrollo, desactiva el reCAPTCHA
        captcha = forms.CharField(required=False)

