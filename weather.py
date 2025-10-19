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

#-------------------------------------------------------------------#
#                          Question One:                            #
#-------------------------------------------------------------------#

# Ask the user to provide an iso string
# get_iso_date_input = input("Enter an ISO date: ")

# Defines a function that will convert the ISO string to readable date
def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    # Use datetime.fromisoformat to convert the string to a date object
    convert_the_date_type = datetime.fromisoformat(iso_string)

    # Use strftime to format the string into "Weekday(%A) Day(%d) Month(%B) Year(%Y)"
    formatted_date = convert_the_date_type.strftime("%A %d %B %Y")

    # Return the reformatted string
    return formatted_date

# Call and print the function with the user's ISO date input
# print(convert_date(get_iso_date_input))

#-------------------------------------------------------------------#
#                          Question Two:                            #
#-------------------------------------------------------------------#

# Ask the user to enter a temperature in Fahrenheit
# get_fahrenheit_input = input("Enter the temperature in fahrenheit: ")

# Define a function that will convert Fahrenheit to Celsius
def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    # Nano Notes: The Formula to convert Fahrenheit to Celsius is °C = (°F - 32) ÷ 1.8

    # Convert the user input into a float so that we can get a decimal result
    inputs = float(temp_in_fahrenheit)

    # Apply the formula
    number = float(inputs - 32)/1.8 

    # Return the converted temperature, rounded to 1 decimal place
    return round(number,1)

# Call and print the function with the user's fahrenheit input
# print(convert_f_to_c(get_fahrenheit_input))

#-------------------------------------------------------------------#
#                          Question Three:                          #
#-------------------------------------------------------------------#

# Get the users list of numbers
# get_mean_list_input = input("Provide a list of numbers: ")

# Create a function to calculate the mean from a list of numbers
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # Nano Notes: The Formula to get the mean is Mean = total of all values ÷ number of values

    # Check that the list provided is empty
    if not weather_data:
        # If the list is empty, return 0
        return 0
    
    # Variable to store the total sum and 
    total_sum = 0.0

    # Variable to store the count of numbers
    count = 0

    # Loop through each value in the list
    for number in weather_data:
        # Convert each value into a float after stripping spaces
        number = float(str(number).strip())
        # Add each number to the running total of numbers in the list
        total_sum += number
        # Counts how many numbers have been processed from the list
        count += 1
        # Apply the mean formula
        mean = total_sum / count
    
    # Return the mean
    return mean

# call and print the function with the user's mean list input
# print(calculate_mean(get_mean_list_input))

#-------------------------------------------------------------------#
#                          Question Four:                           #
#-------------------------------------------------------------------#

# Ask the user to provide the CSV file name or path
# get_csv_file_input = input("Enter the CSV file name (e.g. weather.csv): ")

def load_data_from_csv(csv_file):

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    # Create an empty list to store the weather data
    data = []

    # Open the CSV file in read mode
    with open(csv_file, "r", newline="") as f:
        # Use csv.reader to read the file line by line
        reader = csv.reader(f)

        # Read the first line, which may be a header
        header = next(reader, None)

        # Check if a header exists and if it is not ["date", "min", "max"]
        if header and [h.strip().lower() for h in header] != ["date", "min", "max"]:
            row = header
            if row and any(cell.strip() for cell in row):
                # Extract and clean the date value
                date = row[0].strip()

                # Convert the min and max values via float to int
                min = int(float(row[1]))
                max = int(float(row[2]))

                # Append the cleaned row to the data list
                data.append([date, min, max])

        # Loop through each remaining row in the CSV file
        for row in reader:
            # Skip blank or empty rows
            if not row or not any(cell.strip() for cell in row):
                continue

            # Extract and clean the date value
            date = row[0].strip()

            # Convert the min and max values via float to int
            min = int(float(row[1]))
            max = int(float(row[2]))

            # Append the cleaned row to the data list
            data.append([date, min, max])

    # Return the complete list of weather data
    return data

# Call and print the function with the user's CSV file input
# print(load_data_from_csv(get_csv_file_input))

#-------------------------------------------------------------------#
#                          Question Five:                           #
#-------------------------------------------------------------------#

# # Ask the user to provide a list of numbers
# get_list_of_numbers_min_input = input("Enter a list of numbers separated by commas: ")

# Convert the input string into a list of numbers
# weather_data = [value.strip() for value in get_list_of_numbers_min_input.split(",")]

# Define a function that finds the minimum value and its position in a list
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    # Check if the provided list is empty
    if not weather_data:

        # return a empty tuple because the input list was empty
        return ()
    
    # Create a variable to store the minimum number
    min_number = None

    # Create a variable to store the index
    min_index = None

    # Loop through each number in the list with its index
    for index, number in enumerate(weather_data):

        # Convert the number to float after stripping spaces
        number = float(str(number).strip())

        # Check if min_number is equal to or less than CURRENT min_number
        if min_number is None or number <= min_number:
            # If it is update min_number and min_index
            min_number = number
            min_index = index

    # Return the minimum value and its index as a tuple
    return (float(min_number), min_index)

# Call and print the function with the user's list input
# print(find_min(get_list_of_numbers_min_input))

#-------------------------------------------------------------------#
#                          Question Six:                            #
#-------------------------------------------------------------------#

# Ask the user to provide a list of numbers
# get_list_of_numbers_max_input = input("Enter a list of numbers separated by commas: ")

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    # Check if the list is empty
    if not weather_data:
        # Return an empty tuple if it is
        return ()
    
    # Create a variable to store the minimum number
    max_number = None

    # Create a variable to store the index
    max_index = None

    # Loop through each number in the list with its index
    for index, number in enumerate(weather_data):

        # Strip spaces then turn into a float data type
        number = float(str(number).strip())

        # If max_number is None or bigger than CURRENT max_number
        if max_number is None or number >= max_number:
            # Update the max_number and max_index with it
            max_number = number
            max_index = index
    
    # Return the maximum value and its index as a tuple
    return (float(max_number), max_index)

# Call and print the function with the user's list input
# print(find_min(get_list_of_numbers_max_input))

#-------------------------------------------------------------------#
#                          Question Seven:                          #
#-------------------------------------------------------------------#

# Ask the user to provide the CSV file name or path
# get_csv_file_input = input("Enter the CSV file name (e.g. weather.csv): ")

# Create a function that generates a weather summary from the data
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # Check if the input data is empty and return a default summary
    if not weather_data:
        return "0 Day Overview\n  The lowest temperature will be 0.0°C, and will occur on .\n  The highest temperature will be 0.0°C, and will occur on .\n  The average low this week is 0.0°C.\n  The average high this week is 0.0°C.\n"

    # Extract only the date values from each row of the data
    dates = [row[0] for row in weather_data]

    # Extract and clean the minimum Fahrenheit values from the data
    min_fahrenheit_list = [float(str(row[1]).strip()) for row in weather_data]

    # Extract and clean the maximum Fahrenheit values from the data
    max_fahrenheit_list = [float(str(row[2]).strip()) for row in weather_data]

    # Find the lowest Fahrenheit value and its index position
    min_number_f, min_index = find_min(min_fahrenheit_list)

    # Find the highest Fahrenheit value and its index position
    max_number_f, max_index = find_max(max_fahrenheit_list)

    # Convert the minimum Fahrenheit value to Celsius
    min_number_c = (min_number_f - 32.0) * 5.0 / 9.0

    # Convert the maximum Fahrenheit value to Celsius
    max_number_c = (max_number_f - 32.0) * 5.0 / 9.0

    # Get the ISO date for when the minimum temperature occurred
    min_date_iso = dates[min_index]

    # Get the ISO date for when the maximum temperature occurred
    max_date_iso = dates[max_index]

    # Format the minimum date
    min_date = datetime.fromisoformat(min_date_iso).strftime("%A %d %B %Y")

    # Format the maximum date
    max_date = datetime.fromisoformat(max_date_iso).strftime("%A %d %B %Y")

    # Calculate the average of the minimum temperatures in Celsius
    average_min_c = ((calculate_mean(min_fahrenheit_list) - 32.0) * 5.0 / 9.0)

    # Calculate the average of the maximum temperatures in Celsius
    average_max_c = ((calculate_mean(max_fahrenheit_list) - 32.0) * 5.0 / 9.0)

    # Build the summary string with all calculated information
    summary = (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {min_number_c:.1f}°C, and will occur on {min_date}.\n"
        f"  The highest temperature will be {max_number_c:.1f}°C, and will occur on {max_date}.\n"
        f"  The average low this week is {average_min_c:.1f}°C.\n"
        f"  The average high this week is {average_max_c:.1f}°C.\n"
    )

    # Return the final summary
    return summary

# Call and print function with user input
# print(generate_summary(get_csv_file_input))

#-------------------------------------------------------------------#
#                          Question Eight:                          #
#-------------------------------------------------------------------#

# Get user's csv file name
# get_csv_file_input = input("Enter the CSV file name (e.g. weather.csv): ")

# Load the weather data
# collected_weather_data = load_data_from_csv(csv_file_input)

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # Check if the input data is empty and return an empty string if it is
    if not weather_data:
        return ""

    # Create an empty string to accumulate the daily summaries
    daily_summary = ""

    # Loop through each row (each day's weather data)
    for row in weather_data:

        # Extract the ISO date string from the row
        date_iso = row[0]

        # Extract and clean the minimum Fahrenheit temperature
        min_number_f = float(str(row[1]).strip())

        # Extract and clean the maximum Fahrenheit temperature
        max_number_f = float(str(row[2]).strip())

        # Convert the minimum Fahrenheit value to Celsius
        min_number_c = (min_number_f - 32.0) * 5.0 / 9.0

        # Convert the maximum Fahrenheit value to Celsius
        max_number_c = (max_number_f - 32.0) * 5.0 / 9.0

        # Format the ISO date into a readable format (e.g. Tuesday 06 July 2021)
        date = datetime.fromisoformat(date_iso).strftime("%A %d %B %Y")

        # Add the formatted daily summary to the overall summary string
        daily_summary += (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {min_number_c:.1f}°C\n"
            f"  Maximum Temperature: {max_number_c:.1f}°C\n\n"
        )

    # Return the daily summary
    return daily_summary

# Call and print function with user input
# print(generate_daily_summary(collected_weather_data))