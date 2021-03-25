import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# User enters the city that wants to view the data.
def get_city():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Are you ready for started exploring the data')
    city = ''
    while city.lower not in ['new york', 'chicago', 'washington']:
        city = input(
            'Select the city in the system, New York, Chicago or Washington? \n')
        if city.lower() == 'new york':
            return 'new york city'
        elif city.lower() == 'chicago':
            return 'chicago'
        elif city.lower() == 'washington':
            return 'washington'
        else:
            print('I can\'t find that city, try again\n')
    return city

def get_filter():
    """Filter data according to month, year and without filter"""
    filter = ""
    while filter.lower() not in ['day', 'month', 'none']:
        filter = input(
            'How would you like to filter the data - day or month or no filter. Type \'none\' for no filter\n')
        if filter.lower() not in ['day', 'month', 'none']:
            print('You made a mistake, try again\n')
    return filter

def get_month():
    """Specify the data of the month that I want to see"""
    month = ""
    month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    while month.lower() not in month_dict.keys():
        month = input(
            '\nWhich month data would you like to see - January, February, March, April, May, or June?\n')
        if month.lower() not in month_dict.keys():
            print('You made a mistake, try again\n')
    month = month_dict[month.lower()]
    return month
###
# get data per rental day
def get_day():
    """Specify the data of the month that I want to see"""
    day = ""
    day_dict = {'m': 'Monday', 't': 'Tuesday', 'w': 'Wednesday',
                'th': 'Thursday', 'f': 'Friday', 'sa': 'Saturday', 's': 'Sunday'}
    while day.lower() not in day_dict.keys():
        day = input('Which day would you like to see - M, T, W, Th, F, Sa, S\n')
        if day.lower() not in day_dict.keys():
            print('You made a mistake, try again\n')
    day = day_dict[day.lower()]
    return day
###
# Get data for the most popular month of rent
def popular_month(df):
    """Specify the data of the month that I want to see"""
    print('\nCalculating The Most Popular Month...')
    start_time = time.time()

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    value = int(df['Start Time'].dt.month.mode())
    p_month = months[value - 1]
    print('\nThe most popular month is {}'.format(p_month))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Get the data of the most popular day to rent bicycles
def popular_day(df):
    print('\nCalculating The Most Popular Day...')
    start_time = time.time()

    day = ['Monday', 'Tuesday', 'Wednesday',
           'Thursday', 'Friday', 'Saturday', 'Sunday']
    value = int(df['Start Time'].dt.dayofweek.mode())
    p_day = day[value]
    print('\nThe most popular day is {}'.format(p_day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Get the most popular time to rent bikes
def popular_hour(df):
    print('\nCalculating The Most Popular Hour...')
    start_time = time.time()

    value = int(df['Start Time'].dt.hour.mode())
    print('\nThe most popular hour for start time in 24-hour format is {}'.format(value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Get data on the most popular bike rental station
def popular_station(df):
    print('\nCalculating The Most Commonly Used Start and End Station...')
    start_time = time.time()

    value_start = df['Start Station'].mode().to_string(index=False)
    value_end = df['End Station'].mode().to_string(index=False)
    print('\nThe most commonly used start station is {}'.format(value_start))
    print('\nThe most commonly used end station is {}'.format(value_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Calculation of the most frequent combination in a station of a trip from start to finish
def popular_combo_station(df):
    print('\nCalculating The Most Frequent Combination of Start and End Station...')
    start_time = time.time()

    # creates a 'trip' column which matches the start and end station for the popular_trip() function
    df['trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    value = df['trip'].mode().to_string(index=False)
    print('\nThe most frequent combination of start station and end station is {}'.format(value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Function to calculate the total time of a trip
def travel_time(df):
    print('\nCalculating The Total and Mean Travel Time...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()
    mins, sec = divmod(total_time, 60)
    hour, mins = divmod(mins, 60)
    print('The total travel time is {} hours {} minutes and {} seconds'.format(
        hour, mins, sec))

    mean_time = round(df['Trip Duration'].mean())
    mins, sec = divmod(mean_time, 60)
    # if mins > 60:
    hour, mins = divmod(mins, 60)
    print('The mean travel time is {} hours {} minutes and {} seconds'.format(
        hour, mins, sec))
    # else:
    #print('The mean travel time is {} hours {} minute and {} seconds'.format(hour, mins, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Calculate the total of user types
def count_user(df):
    print('\nCalculating The Total Count of User Types...\n')
    start_time = time.time()

    sub = (df['User Type'] == 'Subscriber').sum()
    cust = (df['User Type'] == 'Customer').sum()
    print('\nThe count of subscriber is {} and Customer is {}'.format(sub, cust))

    us = df['User Type'].value_counts()
    print(us)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Calculate total user by gender
def count_gender(df):
    print('\nCalculating The Total Count of Genders...\n')
    start_time = time.time()

    male = (df['Gender'] == 'Male').sum()
    female = (df['Gender'] == 'Female').sum()
    print('\nThe count of male is {} and female is {}'.format(male, female))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Calculate the year of birth of the users. Obtaining the most recent in time and the most common
def count_dob(df):
    print('\nCalculating The Earliest, Most Recent, and Most Common Year of Birth...\n')
    start_time = time.time()

    dob_early = int(df['Birth Year'].min())
    dob_recent = int(df['Birth Year'].max())
    dob_common = int(df['Birth Year'].mode())
    print('\nThe most earliest year of birth is {}'.format(dob_early))
    print('\nThe most recent year of birth is {}'.format(dob_recent))
    print('\nThe most common year of birth is {}'.format(dob_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###
# Función para desplegar los datos de viajes individuales
def display_data(df):
    """
    Display individual trip data
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    start = 0
    end = 5
    choice = ''
    while choice.lower() not in ['yes', 'no']:
        choice = input(
            'Do you want to view indiviual trip data? Type \'Yes\' or \'No\'\n')
        if choice.lower() not in ['yes', 'no']:
            print('Maybe you made a typo. Please try again\n')
        elif choice.lower() == "yes":
            print(df.iloc[start:end])
            # Write a while loop
            while True:
                sec_choice = input(
                    '\nDo you want to view more trip data? Type \'Yes\' or \'No\'\n')
                if sec_choice.lower() not in ['yes', 'no']:
                    print('Maybe you made a typo. Please try again\n')
                elif sec_choice.lower() == "yes":
                    start += 5
                    end += 5
                    print(df.iloc[start:end])
                elif sec_choice == "no":
                    return
        elif choice.lower() == "no":
            return
    return
###
# main
def main():
    while True:
        # Read city name (New York, Chicago or Washington)
        city = get_city()
        print('Loading data from {} for you...'.format(city))

        # Read csv file for the city selected
        df = pd.read_csv(CITY_DATA[city], parse_dates=[
                         'Start Time', 'End Time'])

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        # Read month and day
        filters = get_filter()
        # if filter == 'none':
        #df = df
        if filters == 'month':
            month = get_month()
            df['month'] = df['Start Time'].dt.month
            df = df[df['month'] == month]
        elif filters == 'day':
            day = get_day()
            df['day'] = df['Start Time'].dt.weekday_name
            df = df[df['day'] == day]

        # Most common month
        if filters == 'none':
            popular_month(df)

        # Most common day
        if filters == 'none' or filters == 'month':
            popular_day(df)

        # Most common hour
        popular_hour(df)

        # Most commonly used start and end station
        popular_station(df)

        # Displays the most frequent combination of start station and end station
        popular_combo_station(df)

        # Displays the total and mean teavel time
        travel_time(df)

        # Displays the count of each user type
        count_user(df)

        if city == 'chicago' or city == 'new york':
            # Displays the count of gender
            count_gender(df)

            # Display earliest, most recent, and most common year of birth
            count_dob(df)

        if city == 'washington':
            print('\nNo gender and birth year data available')

        # Display data info
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
