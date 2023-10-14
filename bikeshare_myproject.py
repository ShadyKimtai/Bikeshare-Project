import time
import pandas as pd
import numpy as np
import time # Import the time module for timing-related operations

#Dictionary to map city names to data files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose a valid city.")

    # Get user input for time filter (month or day or none)
    while True:
        time_filter = input("Would you like to filter the data by month, day, or not at all? ").lower()
        if time_filter in ['month', 'day', 'not at all']:
            break
        else:
            print("Invalid input. Please choose 'month', 'day', or 'not at all'.")

    if time_filter == 'month':
        while True:
            month = input("Which month - January, February, March, April, May, or June? ").lower()
            if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print("Invalid input. Please choose a valid month.")
        day = 'all'
    elif time_filter == 'day':
        while True:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").lower()
            if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                print("Invalid input. Please choose a valid day.")
        month = 'all'
    else:
        month = 'all'
        day = 'all'

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
         # Convert month name to month number and filter DataFrame by that number
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Month'] == month_num]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df

def display_raw_data(df):
    """
    Displays 5 lines of raw data at a time upon user request.
    """
    start_idx = 0
    end_idx = 5

    while True:
        raw_data_display = input("Would you like to see 5 lines of raw data? Enter yes or no: ").lower()
        if raw_data_display == 'yes':
             # Display 5 rows of raw data starting from start_idx and ending at end_idx
            print(df.iloc[start_idx:end_idx])
            start_idx += 5
            end_idx += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
