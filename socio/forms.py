from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    last_name = forms.CharField(label='', max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        del self.fields['password']

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['first_name'].label = ''
        self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>Ingresa tu nombre.</small></span>'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['last_name'].label = ''
        self.fields['last_name'].help_text = '<span class="form-text text-muted"><small>Ingresa tu apellido.</small></span>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>Ingresa una dirección de correo electrónico válida.</small></span>'

