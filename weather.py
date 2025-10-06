import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    convert_the_date_type = datetime.fromisoformat(iso_string)
    formatted_date = convert_the_date_type.strftime("%A %d %B %Y")
    return formatted_date

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    inputs = float(temp_in_fahrenheit)
    number = float(inputs - 32)/1.8 
    return round(number,1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    if not weather_data:
        return 0
    total_sum = 0.0
    count = 0
    for number in weather_data:
        number = float(str(number).strip())
        total_sum += number
        count += 1
    return total_sum / count

def load_data_from_csv(csv_file):

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)

        if header and [h.strip().lower() for h in header] != ["date", "min", "max"]:
            row = header
            if row and any(cell.strip() for cell in row):
                date = row[0].strip()
                try:
                    mn = int(row[1])
                    mx = int(row[2])
                except ValueError:
                    mn = int(float(row[1]))
                    mx = int(float(row[2]))
                data.append([date, mn, mx])

        for row in reader:
            if not row or not any(cell.strip() for cell in row):
                continue
            date = row[0].strip()
            try:
                mn = int(row[1])
                mx = int(row[2])
            except ValueError:
                mn = int(float(row[1]))
                mx = int(float(row[2]))
            data.append([date, mn, mx])
    return data

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    min_number = None
    min_index = None
    for index, number in enumerate(weather_data):
        number = float(str(number).strip())
        if min_number is None or number <= min_number:
            min_number = number
            min_index = index
    return (float(min_number), min_index)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    max_number = None
    max_index = None
    for index, number in enumerate(weather_data):
        number = float(str(number).strip())
        if max_number is None or number >= max_number:
            max_number = number
            max_index = index
    return (float(max_number), max_index)

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "0 Day Overview\n  The lowest temperature will be 0.0°C, and will occur on .\n  The highest temperature will be 0.0°C, and will occur on .\n  The average low this week is 0.0°C.\n  The average high this week is 0.0°C.\n"

    dates = [row[0] for row in weather_data]
    min_fahrenheit_list = [float(str(row[1]).strip()) for row in weather_data]
    max_fahrenheit_list = [float(str(row[2]).strip()) for row in weather_data]

    min_number_f, min_index = find_min(min_fahrenheit_list)
    max_number_f, max_index = find_max(max_fahrenheit_list)

    min_number_c = (min_number_f - 32.0) * 5.0 / 9.0
    max_number_c = (max_number_f - 32.0) * 5.0 / 9.0

    min_date_iso = dates[min_index]
    max_date_iso = dates[max_index]
    min_date = datetime.fromisoformat(min_date_iso).strftime("%A %d July %Y") if "July" in datetime.fromisoformat(min_date_iso).strftime("%B") else datetime.fromisoformat(min_date_iso).strftime("%A %d %B %Y")
    max_date = datetime.fromisoformat(max_date_iso).strftime("%A %d July %Y") if "July" in datetime.fromisoformat(max_date_iso).strftime("%B") else datetime.fromisoformat(max_date_iso).strftime("%A %d %B %Y")

    average_min_c = ((calculate_mean(min_fahrenheit_list) - 32.0) * 5.0 / 9.0)
    average_max_c = ((calculate_mean(max_fahrenheit_list) - 32.0) * 5.0 / 9.0)

    summary = (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {min_number_c:.1f}°C, and will occur on {min_date}.\n"
        f"  The highest temperature will be {max_number_c:.1f}°C, and will occur on {max_date}.\n"
        f"  The average low this week is {average_min_c:.1f}°C.\n"
        f"  The average high this week is {average_max_c:.1f}°C.\n"
    )
    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return ""

    daily_summary = ""

    for row in weather_data:
        date_iso = row[0]
        min_number_f = float(str(row[1]).strip())
        max_number_f = float(str(row[2]).strip())

        min_number_c = (min_number_f - 32.0) * 5.0 / 9.0
        max_number_c = (max_number_f - 32.0) * 5.0 / 9.0

        date = datetime.fromisoformat(date_iso).strftime("%A %d %B %Y")

        daily_summary += (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {min_number_c:.1f}°C\n"
            f"  Maximum Temperature: {max_number_c:.1f}°C\n\n"
        )

    return daily_summary