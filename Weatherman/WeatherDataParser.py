"""
Holds the WeatherDataParser class which reads all valid format files and collects the readings within them
"""

import os
import glob

from WeatherReading import WeatherReading
from helpers import date_mapper, string_splitter
from constants import MURREE


class WeatherDataParser:
    """
    Weather data parser to read weather data files from a directory and filter by date.
    """

    def __init__(self, directory, date):
        """
        Initialize the WeatherDataParser with the given directory and date.

        Args:
            directory (str): The directory containing weather data files.
            date (str): The input date in the format "YYYY/MM" or "YYYY" to filter the data.
        """

        self.directory = directory
        self.weather_data = []      
        self.year = string_splitter(date, 'year', '/')
        self.month = string_splitter(date, 'month', '/') 

    def parse_files(self):
        """
        Parse weather data files and populate the weather_data list with WeatherReading objects.

        The method reads weather data files from the specified directory and filters the data based
        on the provided date. It constructs WeatherReading objects from the valid rows and stores
        them in the weather_data list.

        Returns:
            None
        """
        select_month = "" if self.month == 0 else date_mapper(str(self.month), '%b')
        if select_month:
            file_pattern = f"{MURREE}_{self.year}_{select_month}.txt"
        else:
            file_pattern = f"{MURREE}_{self.year}_*.txt"
        files = glob.glob(os.path.join(self.directory, file_pattern))
        for filename in files:
            with open(filename, 'r') as file:
                next(file)
                for row in file:
                    parts = row.strip().split(",")
                    date = parts[0]
                    temp_high = parts[1]
                    temp_low = parts[3]
                    humidity = parts[8]
                    weather_reading = WeatherReading(date, temp_high, temp_low, humidity)
                    self.weather_data.append(weather_reading)
