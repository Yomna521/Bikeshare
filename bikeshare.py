import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
valid_city = ['chicago', 'new york city', 'washington']
valid_month = ['all', 'january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'september', 'october', 'november', 'december']
valid_day= ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
        city = str(input("Choose name of city (chicago, new york city, washington): ")).lower()
        if city in valid_city:
            break
        else:
            print("Invalid city name - try again") 

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Choose name of month (all, january, february, ... , december): ")).lower()
        if month in valid_month:
            break
        else:
            print("Invalid month name - try again") 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Choose name of day (all, monday, tuesday, ... sunday): ")).lower()
        if day in valid_day:
            break
        else:
            print("Invalid day name - try again") 

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month = valid_month.index(month)
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    try:
        # TO DO: display the most common month
        print("the most common month is {}".format(df['month'].mode().max()))

        # TO DO: display the most common day of week
        print("the most common day of week is {}".format(df['day'].mode().max()))

        # TO DO: display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        print("the most common start hour is {}".format(df['hour'].mode().max()))

    except:
        print("*************An error occurred*************")
	
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
            

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    try:
        # TO DO: display most commonly used start station
        print("The most commonly used start station is {}".format(df['Start Station'].mode().max()))

        # TO DO: display most commonly used end station
        print("The most commonly used end station is {}".format(df['End Station'].mode().max()))

        # TO DO: display most frequent combination of start station and end station trip
        print("The most frequent combination of start station and end station trip are\n{}".format(df[['Start Station', 'End Station']].mode().max()))
	
    except:
        print("*************An error occurred*************")
	
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    try:
        # TO DO: display total travel time
        print("total travel time is {}".format(df["Trip Duration"].sum()))

        # TO DO: display mean travel time
        print("mean travel time is {}".format(df["Trip Duration"].sum()/len(df["Trip Duration"])))

    except:
        print("*************An error occurred*************")
	
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
	
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    try:
        # TO DO: Display counts of user types
        print("The counts of user types are\n{}".format(df['User Type'].value_counts()))

        # TO DO: Display counts of gender
        print("The counts of genders are\n{}".format(df['Gender'].value_counts()))
    
        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth is {}".format(df['Birth Year'].min()))
        print("The most recent year of birth is {}".format(df['Birth Year'].max()))
        print("The most common year of birth is {}".format(df['Birth Year'].mode().max()))

    except:
        print("*************An error occurred*************")
	
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
	
def display_data(df):
    """Displays rows of data from the dataframe to the user"""
    display = input('\nWould you like to view the first 5 rows of data? Enter yes or no.\n').lower()
    
    loc = 0
    while(display == 'yes'):
	start_time = time.time()
        for _ in range(5):
            print(df.iloc[loc])
            loc += 1
    	print("\nThis took %s seconds." % (time.time() - start_time))
	display = input("Do you wish to view the next 5 rows of data? Enter yes or no.\n").lower()   
    print('-'*40)
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        #Trip statistics
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
