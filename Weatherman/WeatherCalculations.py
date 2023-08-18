"""
Holds the WeatherCalculations class which holds calculation funtions for the weather readings
"""

class WeatherCalculations:
    """
    Class to perform various calculations on weather data.

    Attributes:
        weather_data (list): A list of WeatherReading objects containing weather data.
    """

    def __init__(self, weather_data):
        """
        Initialize the WeatherCalculations with the provided weather data.

        Args:
            weather_data (list): A list of WeatherReading objects containing weather data.
        """

        self.weather_data = weather_data

    def get_highest_temperature_record(self):
        """
        Get the highest temperature and its corresponding date from the weather data.

        Returns:
            tuple: A tuple containing the highest temperature and its corresponding date in the format "YYYY-MM-DD".
        """

        highest_temp = max(self.weather_data, key=lambda x: x.temp_high 
                           if x.temp_high is not None else float('-inf'))
        return highest_temp.temp_high, highest_temp.date

    def get_lowest_temperature_record(self):
        """
        Get the lowest temperature and its corresponding date from the weather data.

        Returns:
            tuple: A tuple containing the lowest temperature and its corresponding date in the format "YYYY-MM-DD".
        """

        lowest_temp = min(self.weather_data, key=lambda x: x.temp_low
                          if x.temp_low is not None else float('inf'))
        return lowest_temp.temp_low, lowest_temp.date

    def get_most_humid_day_record(self):
        """
        Get the day with the highest humidity and its corresponding date from the weather data.

        Returns:
            tuple: A tuple containing the highest humidity and its corresponding date in the format "YYYY-MM-DD".
        """

        most_humid = max(self.weather_data, key=lambda x: x.humidity
                         if x.humidity is not None else float('-inf'))
        return most_humid.humidity, most_humid.date
    
    def get_average_highest_temperature(self):
        """
        Get the average highest temperature from the weather data.

        Returns:
            float: The average highest temperature.
        """

        avg_highest_temp = sum([reading.temp_high for reading in self.weather_data 
                                if reading.temp_high is not None]) / len(self.weather_data)
        return avg_highest_temp
    
    def get_average_lowest_temperature(self):
        """
        Get the average lowest temperature from the weather data.

        Returns:
            float: The average lowest temperature.
        """

        avg_lowest_temp = sum([reading.temp_low for reading in self.weather_data 
                               if reading.temp_low is not None]) / len(self.weather_data)
        return avg_lowest_temp
    
    def get_average_mean_humidity(self):
        """
        Get the average mean humidity from the weather data.

        Returns:
            float: The average mean humidity.
        """

        avg_humidity = sum([reading.humidity for reading in self.weather_data 
                            if reading.humidity is not None]) / len(self.weather_data)
        return avg_humidity
    