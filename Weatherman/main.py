"""
Holds main function to handle command line arguments and initiate report generation
"""

import argparse

from helpers import execute
from WeatherDataParser import WeatherDataParser
from WeatherReports import WeatherReports


def main():
    """
    Main function to handle command line arguments and display weather data reports.

    Command line arguments:
        "directory" (str): Path to the directory containing weather data files.
        "-e", "--high_low" (str): Display highest, lowest, and most humid day for a given year (format: "YYYY").
        "-a", "--average" (str): Display average highest, lowest, and mean humidity for a given month (format: "YYYY/MM").
        "-c", "--chart" (str): Draw horizontal bar charts for highest and lowest temperatures for a given month (format: "YYYY/MM").

    Returns:
        None
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Path to the directory containing weather data files.")
    parser.add_argument("-e", "--high_low", type=str, help="Display highest, lowest, and most humid day for a given year.")
    parser.add_argument("-a", "--average", type=str, help="Display average highest, lowest, and mean humidity for a given month.")
    parser.add_argument("-c", "--chart", type=str, help="Draw horizontal bar charts for highest and lowest temperatures for a given month.")
    args = parser.parse_args()
    
    if args.high_low:
        data_parser = WeatherDataParser(args.directory, args.high_low)
        data_parser.parse_files()
        display_dict=execute(args.high_low, data_parser, "e")
        WeatherReports.create_high_low_temp_report(display_dict)
    if args.average:
        data_parser = WeatherDataParser(args.directory, args.average)
        data_parser.parse_files()
        display_dict=execute(args.average, data_parser, "a")
        WeatherReports.create_average_report(display_dict)
    if args.chart:
        data_parser = WeatherDataParser(args.directory, args.chart)
        data_parser.parse_files()
        execute(args.chart, data_parser, "c")
        WeatherReports.create_weather_chart(data_parser.weather_data)
        
if __name__ == "__main__":
    main()
