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
    city = input("Choose the city: chicago, new york city or washington ").lower() #uses lower case letters to match the city names
    while True:
        if city in CITY_DATA:
            print("You Choose {}".format(city))
    # TO DO: get user input for month (all, january, february, ... , june)
            month = input("Choose a Month between january to june or all ").lower() #uses lower case letters to match the month names
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input("Choose a Day (eg. sunday, monday,...) or all ").title()    #uses title to match the day names
            return city, month, day
        else:
            print("{} doesn’t exist in the database, please choose another city".format(city))
            city = input("Enter name of the city ")
        print('-'*40)
                
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
    df = pd.read_csv(CITY_DATA[city])                                     # loads the data file into the dataframe
    df['Start Time'] = pd.to_datetime(df['Start Time'])                   # converts the Start Time column to datetime
    df['month'] = df['Start Time'].dt.month                               # extracts the month to create new column
    df['day_of_week'] = df['Start Time'].dt.weekday_name                  # extracts the day of week to create new column
    df['hour']=df['Start Time'].dt.hour                                   # extracts the time to create new column
    if month != 'all':                                                    # filters by month if applicable
        months = ['january', 'february', 'march', 'april', 'may', 'june'] # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        df = df[df['month'] == month]                                     # filters by month to create the new dataframe
    if day != 'all':                                                      # filters by day of week if applicable
        df = df[df['day_of_week'] == day.title()]                         # filter by day of week to create the new dataframe
    return df

def view_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ")
    start_loc = 0
    end_loc = 5
    while (view_data == 'yes'):
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc +=5
        view_display = input("Do you wish to continue? yes or no. \n ").lower()
        if view_display == "no":
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is {}".format(common_month),"\n")
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is {}".format(common_day),"\n")
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour of the day is {}".format(common_hour),"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print("The most common Start Station is {}".format(common_start_st),"\n")

    # TO DO: display most commonly used end station
    common_end_st = df['End Station'].mode()[0]
    print("The most common End Station is {}".format(common_end_st),"\n")

    # TO DO: display most frequent combination of start station and end station trip
    common_combination_st = (df['Start Station']+";"+ df['End Station']).mode()
    print("The most common combination of Start Station and End Station is {}".format(common_start_st),"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is ",format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is ",format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The count of user types is ","\n",df['User Type'].value_counts(),"\n")
    
    # TO DO: Display counts of gender
    if 'Gender' in df:                               #to check if the gender column does not exist and prevent errors
        print("The count of the Gender of Users is ","\n",df['Gender'].value_counts(),"\n")
    else:
        print("Gender stats cannot be calculated because Gender data is not in the dataframe")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:                          #to check if the birth column does not exist and prevent errors
        print("The earliest birth year of users is ","\n", df['Birth Year'].min(),"\n")
        print("The most resent birth year of users is ","\n", df['Birth Year'].max(),"\n")
        print("The most common birth year of users is ","\n", df['Birth Year'].mode(),"\n")
    else:
        print('Birth stats cannot be calculated because Birth data is not in the dataframe')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
