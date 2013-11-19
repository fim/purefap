from django.core.management.base import BaseCommand, CommandError
from purefap.core.models import FTPUser, FTPStaff, FTPClient
from datetime import datetime
from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--noop',
            action='store_true',
            dest='noop',
            default=False,
            help='Just print which users will be set to inactive'),
        )
    help = 'Marks users that are past their expiry period as inactive'

    def handle(self, *args, **options):
        for u in FTPUser.objects.all():
            if u.expiry_date and u.expiry_date.isocalendar() < datetime.now().isocalendar():
                self.stdout.write("User %s is past the expiration date" % u)
                if not options['noop']:
                    u.is_active = False
                    u.save()

        for u in FTPClient.objects.all():
            if u.expiry_date and u.expiry_date.isocalendar() < datetime.now().isocalendar():
                self.stdout.write("User %s is past the expiration date" % u)
                if not options['noop']:
                    u.is_active = False
                    u.save()

        for u in FTPStaff.objects.all():
            if u.expiry_date and u.expiry_date.isocalendar() < datetime.now().isocalendar():
                self.stdout.write("User %s is past the expiration date" % u)
                if not options['noop']:
                    u.is_active = False
                    u.save()
