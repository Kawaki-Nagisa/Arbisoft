import pytz
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from time_app.models import PSTDateTime

class Command(BaseCommand):
    """
    Management command to insert dummy users and PST date times into the database.
    
    This command creates a specified number of dummy user accounts and inserts corresponding
    Pacific Standard Time (PST) date times into the database.

    Attributes:
        help (str): A brief description of the command's purpose.

    Methods:
        handle(*args, **options): The main function that gets executed when the command is run.
    """

    help = 'Inserts dummy users and PST date times into the database'

    def handle(self, *args, **options):
        """
        Execute the command to insert dummy data into the database.

        This function creates a specified number of dummy user accounts and inserts corresponding
        Pacific Standard Time (PST) date times into the database.

        Args:
            *args: Additional arguments passed to the command.
            **options: Additional keyword arguments passed to the command.

        Returns:
            None
        """
        for i in range(100):
            User.objects.create(username=f'user_{i}')

        start_datetime = datetime(2022, 8, 28, 12, 0, 0) 
        timezone = pytz.timezone('US/Pacific')
        start_datetime = timezone.localize(start_datetime)
        
        for i in range(100):
            current_datetime = start_datetime + timedelta(hours=i)
            PSTDateTime.objects.create(datetime_field=current_datetime, tz="PST")

        self.stdout.write(self.style.SUCCESS('Successfully inserted dummy data'))
