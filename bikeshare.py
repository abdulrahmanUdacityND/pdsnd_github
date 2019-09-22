# Disclaimer:
# these online pages helped me gitting through this project:
# http://www.datasciencemadesimple.com/mean-function-python-pandas-dataframe-row-column-wise-mean/
# https://www.programiz.com/python-programming/methods/list/index
# https://www.stechies.com/python-print-without-newline/
# https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python
# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/#iloc-selection

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    flag = 1;
    while(flag):
        print("Please choose a city: chicago, new york city, or washington")
        city = input().lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        print("Sorry, Invalid input")
    
    print("Valid input")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    flag = 1;
    while(flag):
        print("Please choose a month (from january to june), or type 'all'")
        month = input().lower()
        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
            break
        print("Sorry, Invalid input")
    
    print("Valid input")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    flag = 1;
    while(flag):
        print("Please choose a day (from sunday to saturday), or type 'all'")
        day = input().lower()
        if day == 'sunday' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'all':
            break
        print("Sorry, Invalid input")
    
    print("Valid input")
    
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[popular_month-1]
    print ('the most popular month is ')
    print(popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print ('\nthe most popular day of the week is ')
    print(popular_day)
    
    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print ('\nthe most popular hour of the day is ')
    print(popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print ('\nthe most popular start station is ')
    print(popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print ('\nthe most popular end station is ')
    print(popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print ('\nthe most frequent combination of start station and end station trip is ')
    print(df.groupby(['Start Station','End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTripDuration = df.loc[:,"Trip Duration"].sum()
    print('\ntotal trip durations is ')
    print(totalTripDuration , end = '')
    print(' minutes')
    
    # TO DO: display mean travel time
    print('\nmean trip duration is ')
    meanTripDuration = df.loc[:,"Trip Duration"].mean()
    print(meanTripDuration , end = '')
    print(' minutes')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("counts user types")
    print(user_types)

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print("\ngender stat.")
    except:
        print("\nNo gender stat.")
    
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nearliest year:')
        print(int(earliest_year))
        latest_year = df['Birth Year'].max()
        print('\nmost recent year:')
        print(int(latest_year))
        popular_year = df['Birth Year'].mode()[0]
        print('\nmost common year:')
        print(int(popular_year))
    except:
        print("\nNo years stat.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def print_raw_data(df):
    max = 4
    min = 0
    while True:
        print(df.iloc[min:max])
        restartRawInput = input('\nWould you like to display more data? Enter yes or no.\n')
        if restartRawInput.lower() != 'yes':
            break
        else:
            min += 5
            max += 5
        
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        enterDisplayFunctionFlag = input('\nWould you like to display raw data? Enter yes or no.\n')
        if enterDisplayFunctionFlag.lower() == 'yes':
            print_raw_data(df)
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
