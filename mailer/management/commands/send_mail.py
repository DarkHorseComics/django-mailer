import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from mailer.engine import send_all


# allow a sysadmin to pause the sending of mail temporarily.
PAUSE_SEND = getattr(settings, "MAILER_PAUSE_SEND", False)


class Command(BaseCommand):
    help = "Do one pass through the mail queue, attempting to send all mail."

    def add_arguments(self, parser):
        parser.add_argument('-q', '--quiet', dest='quiet', default=False,
            action='store_true', help='Silence output unless an error occurs.')
    
    def handle(self, **options):
        quiet = options.get('quiet', False)

        # Set logging level if quiet
        if quiet:
            logging.disable(logging.INFO)

        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        logging.info("-" * 72)
        # if PAUSE_SEND is turned on don't do anything.
        if not PAUSE_SEND:
            send_all()
        else:
            logging.info("sending is paused, quitting.")
