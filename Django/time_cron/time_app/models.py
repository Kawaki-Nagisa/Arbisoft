from django.db import models

class PSTDateTime(models.Model):
    """
    Model to store date times and corresponding time zones.
    
    This model stores date times along with their corresponding time zones.
    The 'datetime_field' field holds the date and time, while the 'tz' field holds
    the abbreviation of the time zone.

    Fields:
        datetime_field (DateTimeField): The date and time to be stored.
        tz (CharField): The abbreviation of the time zone.

    Methods:
        None
    """
    datetime_field = models.DateTimeField()
    tz = models.CharField(max_length=3)
