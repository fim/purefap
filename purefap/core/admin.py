from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from purefap.core.models import FTPClient, FTPUser, FTPStaff
from purefap.core.forms import *

class FTPUserAdmin(UserAdmin):
    form = FTPUserChangeForm
    add_form = FTPUserAddForm
    fieldsets = (
            ('User Info', {
                'fields' : ('username', 'password', 'company',)
               # 'first_name', 'last_name', 'email',)
                }),
            ('FTP Info', {
                'fields' : ('ftpuid', 'ftpgid', 'download_limit', 'upload_limit', 'quota', 'ip_address', 'expiry_date','homedir',) 
                }),
            ('User permissions', {
                'fields' : ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions',)
                }),
        )

    def queryset(self, request):
        return self.model.objects.filter(is_staff=True, is_superuser=False)

class FTPClientAdmin(UserAdmin):
    form = FTPClientChangeForm
    add_form = FTPClientAddForm
    fieldsets = (
            ('User Info', {
                'fields' : ('username', 'password', 'company',)
               # 'first_name', 'last_name', 'email',)
                }),
            ('FTP Info', {
                'fields' : ('ftpuid', 'ftpgid', 'download_limit', 'upload_limit', 'quota', 'ip_address', 'expiry_date','homedir',) 
                }),
            ('User permissions', {
                'fields' : ('is_active',)
                }),
        )

    def queryset(self, request):
        return self.model.objects.filter(is_staff=False)

class FTPStaffAdmin(UserAdmin):
    form = FTPStaffChangeForm
    add_form = FTPStaffAddForm
    fieldsets = (
            ('User Info', {
                'fields' : ('username', 'password', 'company',)
               # 'first_name', 'last_name', 'email',)
                }),
            ('FTP Info', {
                'fields' : ('ftpuid', 'ftpgid', 'download_limit', 'upload_limit', 'quota', 'ip_address', 'expiry_date','homedir',) 
                }),
            ('User permissions', {
                'fields' : ('is_superuser', 'is_active', 'groups', 'user_permissions',)
                }),
        )

if settings.COMPLEX_MODE:
    admin.site.register(FTPClient, FTPClientAdmin)
    admin.site.register(FTPStaff, FTPStaffAdmin)
else:  
    admin.site.register(FTPUser, FTPUserAdmin)

