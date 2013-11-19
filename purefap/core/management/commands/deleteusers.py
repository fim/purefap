from django.core.management.base import BaseCommand, CommandError
from purefap.core.models import FTPUser, FTPStaff, FTPClient
import shutil
from datetime import datetime
from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--noop',
            action='store_true',
            dest='noop',
            default=False,
            help='Just print which users will be deleted'),
        make_option('--files',
            action='store_true',
            dest='files',
            default=False,
            help='Delete user\'s homedir along with his account')
        )
    help = 'Delete expired/inactive users' 

    def handle(self, *args, **options):
        for u in FTPUser.objects.all():
            if u.expiry_date and u.expiry_date.isocalendar() < datetime.now().isocalendar():
                self.stdout.write("User %s will be deleted" % u)
                if options ['files']:
                    self.stdout.write(" - Directory %s and its contents will be deleted" % u.homedir)
                if not options['noop']:
                    if options['files']:
                        shutil.rmtree(u.homedir)
                    u.delete()

        for u in FTPClient.objects.all():
            if u.expiry_date and u.expiry_date.isocalendar() < datetime.now().isocalendar():
                self.stdout.write("User %s will be deleted" % u)
                if options ['files']:
                    self.stdout.write(" - Directory %s and its contents will be deleted" % u.homedir)
                if not options['noop']:
                    if options['files']:
                        shutil.rmtree(u.homedir)
                    u.delete()

        for u in FTPStaff.objects.all():
            if u.expiry_date and u.expiry_date.isocalendar() < datetime.now().isocalendar():
                self.stdout.write("User %s will be deleted" % u)
                if options ['files']:
                    self.stdout.write(" - Directory %s and its contents will be deleted" % u.homedir)
                if not options['noop']:
                    if options['files']:
                        shutil.rmtree(u.homedir)
                    u.delete()
