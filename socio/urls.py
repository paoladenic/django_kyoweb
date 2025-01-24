from django.urls import path
from .views import *

app_name = 'socio'

urlpatterns = [
    path('', home, name='home'),
    path('logout/', LogoutView.as_view(next_page='web:home'), name='logout'),
    path('edit_profile/', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('edit_profile_done/', TemplateView.as_view(template_name='socio/edit_profile_done.html'), name='edit_profile_done'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='socio/change_password_done.html'), name='password_change_done'),
]
