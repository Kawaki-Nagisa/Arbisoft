"""
Holds helper functions for date mapping and string splitting and report executtion
"""

from WeatherCalculations import WeatherCalculations
from constants import MONTHS_FULL_NAME, MONTHS_SHORT_NAME


def date_mapper(date, output_format):
    """
    Map the input date to a formatted string based on the specifier.

    Arguments:
        date (str): The input date in the format "YYYY-MM-DD".
        output_format (str): The specifier for the date format.

    Returns:
        formatted_date: The formatted date string.
    """
    
    try:
        components = date.split('-')
        year = components[0]
        month = components[1] if len(components) > 1 else '01'
        day = components[2] if len(components) > 2 else '01'
        formatted_date = output_format.replace('%Y', str(year))
        formatted_date = formatted_date.replace('%d', str(day).zfill(2))
        formatted_date = formatted_date.replace('%B', MONTHS_FULL_NAME[int(month) - 1])
        formatted_date = formatted_date.replace('%b', MONTHS_SHORT_NAME[int(month) - 1])
        return formatted_date
    except ValueError:
        return "Invalid input date format. Please use 'YYYY-MM-DD'."


def execute(date, data_parser, report_type):
        """
        Execute weather data reports based on the provided date, directory, and specifier.

        Args:
            date (str): The date in the format "YYYY/MM" or "YYYY".
            data_parser (WeatherDataParser): Object which holds the parsed data raedings.
            report_type (str): The specifier indicating the type of report to generate.
                            Possible values: "e" for high/low/humidity, "a" for averages, "c" for chart.

        Returns:
            None
        """

        weather_calculator = WeatherCalculations(data_parser.weather_data)
        if report_type ==  "e":
            highest_temp, highest_date = weather_calculator.get_highest_temperature_record()
            lowest_temp, lowest_date = weather_calculator.get_lowest_temperature_record()
            humidity, humid_date = weather_calculator.get_most_humid_day_record()
            data_dict = {
            "highest_temp": highest_temp,
            "highest_date": highest_date,
            "lowest_temp": lowest_temp,
            "lowest_date": lowest_date,
            "humidity": humidity,
            "humid_date": humid_date
            }
            return data_dict
        elif report_type == "a":
            average_highest_temp = weather_calculator.get_average_highest_temperature()
            average_lowest_temp = weather_calculator.get_average_lowest_temperature()
            average_humidity = weather_calculator.get_average_mean_humidity()
            data_dict = {
            "average_highest_temp": average_highest_temp,
            "average_lowest_temp": average_lowest_temp,
            "average_humidity": average_humidity
            }
            return data_dict
        elif report_type == "c":
            year, month = map(int, date.split('/'))
            print(f"{date_mapper(str(month), '%B')} {year}")
            

def string_splitter(line, choice, splitter):
    """
    Split the argument string into parts
    
    Args:
            line (str): String holding
            choice (str): choice of what to return either year or month from the string
            splitter (str): the character to split around 

        Returns:
            (int) : year or month and if month is invalid return 0.
    """

    parts = line.split(splitter)
    if choice == 'year':
        return int(parts[0])
    elif choice == 'month':
        return int(parts[1]) if len(parts) == 2 else 0

def display_reading(heading, value, date=None):
    """
    Split the argument string into parts
    
    Args:
            heading (str): Name attributed to the reading.
            value (int or float): The value of the reading.
            date (str, optional): The date of the raeding. 

        Returns:
            None.
    """

    if date is None:
        print(f"{heading}: {value:.1f}{'%' if 'Humidity' in heading else 'C'}")
    else:    
        print(f"{heading}: {value}{'%' if 'Humidity' in heading else 'C'} on {date_mapper(date, '%B %d')}")

def display_bar_chart(date, bars, temp_low, temp_high):
    print(f"{date} {bars} {temp_low}C-{temp_high}C")
    