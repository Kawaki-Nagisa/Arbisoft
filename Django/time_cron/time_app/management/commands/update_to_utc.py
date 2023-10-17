import pytz
from django.core.management.base import BaseCommand
from time_app.models import PSTDateTime


class Command(BaseCommand):
    """
    Management command to update selected date times to Coordinated Universal Time (UTC).
    
    This command retrieves instances of PSTDateTime model with the 'tz' field set to a value
    other than UTC, and converts their datetime fields to Coordinated Universal Time (UTC).
    It then updates the 'tz' field accordingly.

    Methods:
        handle(*args, **options): The main function that gets executed when the command is run.
    """

    def handle(self, *args, **options):
        """
        Execute the command to update selected date times to UTC.

        This function retrieves instances of PSTDateTime model with the 'tz' field set to a value
        other than UTC, and converts their datetime fields to Coordinated Universal Time (UTC).
        It then updates the 'tz' field accordingly.

        Args:
            *args: Additional arguments passed to the command.
            **options: Additional keyword arguments passed to the command.

        Returns:
            None
        """
        utc_timezone = pytz.timezone('UTC')
        updated_count = 0
        for date_instance in PSTDateTime.objects.all():
            if date_instance.tz == "UTC":
                continue
            if updated_count >= 10:
                break
            date_instance.datetime_field = date_instance.datetime_field.astimezone(utc_timezone)
            date_instance.tz = "UTC"
            date_instance.save()
            updated_count += 1
        self.stdout.write(self.style.SUCCESS('Updated to UTC'))
