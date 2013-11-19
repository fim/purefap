import os
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.utils.encoding import force_str
from purefap.core.models import FTPClient, FTPUser, FTPStaff
from filebrowser.widgets import FileInput

class FTPUserAddForm(forms.ModelForm):

    password1 = forms.CharField(label=_("Password"),
                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                widget=forms.PasswordInput,
                help_text = _("Enter the same password as above, for verification."))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(FTPUserAddForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = FTPUser


class FTPUserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(label= ("Password"),
        help_text= ("Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            "using <a href=\"password/\">this form</a>."))

    def clean_homedir(self):
        homedir = self.cleaned_data.get("homedir", "")
        homeroot = settings.FTP_CHROOT
        if homedir and not os.path.isdir(os.path.join(homeroot, homedir)):
            raise forms.ValidationError(
                self.error_messages['Selection is not a folder'])

        return os.path.join(homeroot, homedir)

    def clean_password(self):
        return self.initial["password"]

    class Meta:
        model = FTPUser

class FTPClientAddForm(FTPUserAddForm):

    class Meta:
        model = FTPClient

class FTPClientChangeForm(FTPUserChangeForm):

    class Meta:
        model = FTPClient

class FTPStaffAddForm(FTPUserAddForm):

    class Meta:
        model = FTPStaff 

class FTPStaffChangeForm(FTPUserChangeForm):

    class Meta:
        model = FTPStaff 
