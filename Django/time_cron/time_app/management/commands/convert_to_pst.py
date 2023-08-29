import pytz
from django.core.management.base import BaseCommand
from time_app.models import PSTDateTime

class Command(BaseCommand):
    """
    Management command to convert date times to Pacific Standard Time (PST).
    
    This command retrieves all instances of PSTDateTime model, converts their datetime fields
    to Pacific Standard Time (PST) and updates the 'tz' field accordingly.

    Methods:
        handle(*args, **options): The main function that gets executed when the command is run.
    """

    def handle(self, *args, **options):
        """
        Execute the command to convert date times to PST.

        This function retrieves all instances of PSTDateTime model, converts their datetime fields
        to Pacific Standard Time (PST) and updates the 'tz' field accordingly.

        Args:
            *args: Additional arguments passed to the command.
            **options: Additional keyword arguments passed to the command.

        Returns:
            None
        """
        pst_timezone = pytz.timezone('US/Pacific')
        for date_instance in PSTDateTime.objects.all():
            date_instance.datetime_field = date_instance.datetime_field.astimezone(pst_timezone)
            date_instance.tz = "PST"
            date_instance.save()
        self.stdout.write(self.style.SUCCESS('Converted to PST'))
