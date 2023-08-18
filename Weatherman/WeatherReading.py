"""
Holds the WeatherReading class which populates each reading
"""

class WeatherReading:
    """
    Class to hold weather readings for a single day.
    """

    def __init__(self, date, temp_high, temp_low, humidity):
        """
        Initialize the WeatherReading with the provided weather data for a single day.

        Args:
            date (str): Date of the weather reading in the format "YYYY-MM-DD".
            temp_high (int): Highest temperature for the day in Celsius.
            temp_low (int): Lowest temperature for the day in Celsius.
            humidity (int): Humidity for the day as a percentage.
        """
        
        self.date = date
        try:
            self.temp_high = int(temp_high)
        except ValueError:
            self.temp_high = None        
        try:
            self.temp_low = int(temp_low)
        except ValueError:
            self.temp_low = None
        try:
            self.humidity = int(humidity)
        except ValueError:
            self.humidity = None  
