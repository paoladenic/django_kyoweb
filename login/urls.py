from django.urls import path
from django.contrib.auth.views import *
from .views import *

app_name = 'login'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='web:home'), name='logout'),
    path('membership-application/', membership_application_view, name='membership_application'),
    path('membership-confirmation/', membership_application_confirmation_view, name='membership_application_confirmation'),
    
    # Password reset URLs
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


