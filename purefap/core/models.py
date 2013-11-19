import os
import crypt

from django.db import models
from django.conf import settings
from django.forms import CharField, Form, PasswordInput
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from filebrowser.fields import FileBrowseField
from datetime import datetime, timedelta

class FTPUser(AbstractUser):

    company = models.CharField(max_length=50, blank=True)
    homedir = FileBrowseField(max_length=256, blank=False)
    quota = models.IntegerField(_("Size Quota (MB)"), help_text=_("Size quota for the user (MB)"),default=0)
    upload_limit = models.IntegerField(_("Upload Limit (Kb/s)"), help_text=_("Upload limit (Kb/s)"),default=0)
    download_limit = models.IntegerField(_("Download Limit (Kb/s)"), help_text=_("Download limit (Kb/s)"),default=0)
    ip_address = models.CharField(_("IP Address"), max_length=15, help_text=_("IP Address"),default="*")
    expiry_date = models.DateTimeField(_("Expiry date"), null=True, blank=True)
    ftppass = models.CharField(max_length=50, blank=False, null=False, editable=False)
    ftpuid = models.IntegerField(_("User ID"), help_text=_("Size quota for the user (MB)"),default=0)
    ftpgid = models.IntegerField(_("Group ID"), help_text=_("Size quota for the user (MB)"),default=0)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.set_ftppass(raw_password)

    def set_ftppass(self, raw_password):
        self.ftppass = crypt.crypt(raw_password, get_random_string(2))

    def __unicode__(self):
        return self.username

    def __repr__(self):
        return repr(u'<FTPUser: %s>' % self.username)

    class Meta:
        verbose_name = 'FTP User'
        verbose_name_plural = 'FTP Users'

class FTPClient(FTPUser):

    def __repr__(self):
        return repr(u'<FTPClient: %s>' % self.username)

    def save(self, *args, **kwargs):
        self.is_staff = False
        self.is_superuser = False
        
        if self.pk is None and settings.USER_EXPIRY_DAYS is not 0:
            self.expiry_date = datetime.now()+timedelta(days=settings.USER_EXPIRY_DAYS)

        if not self.homedir:
            self.homedir = "{}/{}".format(settings.FTP_CHROOT, self.username)
            if not os.path.isdir(self.homedir.path):
                os.mkdir(self.homedir.path)

        super(FTPClient, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'FTP Client'
        verbose_name_plural = 'FTP Clients'

class FTPStaff(FTPUser):

    def __repr__(self):
        return repr(u'<FTPStaff: %s>' % self.username)

    def save(self, *args, **kwargs):
        self.is_staff = True

        if not self.homedir:
            self.homedir = settings.FTP_CHROOT

        super(FTPStaff, self).save(*args, **kwargs)

        try:
            g = Group.objects.get(name='FTP Staff')
        except DoesNotExist:
            pass
        else: 
            self.groups.add(g)
        
    class Meta:
        verbose_name = 'FTP Staff'
        verbose_name_plural = 'FTP Staff'
