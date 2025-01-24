from django.contrib import admin
from .models import MembershipApplication

@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'membership_number', 'is_approved']
    list_filter = ['is_approved']
