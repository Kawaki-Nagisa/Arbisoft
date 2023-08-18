from helpers import date_mapper, display_reading, display_bar_chart
from constants import RED_COlOR, BLUE_COlOR, DEFAULT_COlOR

"""
Holds the WeatherReports class which generates reports according to format
"""

class WeatherReports:
    """
    Class to print the weather reports
    """

    def create_high_low_temp_report(display_dict):
        """
        Print the highest, lowest temperatures, and humidity with their corresponding dates.

        Args:
            highest_temp (int): The highest temperature.
            highest_date (str): The date corresponding to the highest temperature in the format "YYYY-MM-DD".
            lowest_temp (int): The lowest temperature.
            lowest_date (str): The date corresponding to the lowest temperature in the format "YYYY-MM-DD".
            humidity (int): The humidity value.
            humid_date (str): The date corresponding to the humidity reading in the format "YYYY-MM-DD".

        Returns:
            None
        """

        display_reading("Highest", display_dict["highest_temp"], display_dict["highest_date"])
        display_reading("Lowest", display_dict["lowest_temp"], display_dict["lowest_date"])
        display_reading("Humidity", display_dict["humidity"], display_dict["humid_date"])

    def create_average_report(display_dict):
        """
        Print the average highest temperature, average lowest temperature, and average mean humidity.

        Args:
            average_highest_temp (float): The average highest temperature.
            average_lowest_temp (float): The average lowest temperature.
            average_humidity (float): The average mean humidity.

        Returns:
            None
        """

        display_reading("Average Highest Temp", display_dict["average_highest_temp"])
        display_reading("Average Lowest Temp", display_dict["average_lowest_temp"])
        display_reading("Average Mean Humidity", display_dict["average_humidity"])

    def create_weather_chart(weather_data):
        """
        Print a chart displaying temperature ranges for each date in the weather data.

        Args:
            weather_data (list): A list of WeatherReading objects containing weather data.

        Returns:
            None
        """

        for reading in weather_data:
            low_bars = '+' * reading.temp_low if reading.temp_low is not None else 0
            high_bars = '+' * (reading.temp_high - reading.temp_low) if reading.temp_low is not None and reading.temp_high is not None else 0
            date_formatted = date_mapper(reading.date, '%d')
            temp_bars = f"{BLUE_COlOR}{low_bars}{RED_COlOR}{high_bars}{DEFAULT_COlOR}"
            display_bar_chart(date_formatted, temp_bars, reading.temp_low, reading.temp_high)
