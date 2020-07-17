import time
import pandas as pd

# Dictionary that contains data for the three cities: Chicago, New York City, Washington
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# This function gets the users' inputs as filters for the data
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Using a while loop to handle invalid inputs
    while True:
    # Getting the users' input and storing it into a variable while choosing the appropiate object type and transforming it into lower
        city = str(input("\nWhich city would you like data from? Choose from Chicago, New York City or Washington.\n").lower())
        print("\nYou've selected: {}\n".format(city.title()))
    # Using a conditional statement to protect the user against unwanted errors
        if city not in ("new york city", "chicago", "washington", "all"):
            print("\nSorry, you'll have to re-write the city name. Make sure you enter it correctly\n")
            continue
        else:
            break

    # Using a while loop to handle invalid inputs
    while True:
    # Getting the users' input and storing it into a variable while choosing the appropiate object type and transforming it into lower
        month = str(input("\nFilter data by month month: All, January, February, March, April, May, June.  (Please write full month name)\n").lower())
        print("\nYou've selected: {}\n".format(month.title()))
    # Using a conditional statement to protect the user against unwanted errors
        if month not in ("all", "january", "february", "march", "april", "may", "june"):
            print("\nOops, you'll have to re-write the month name. Make sure you enter it correctly\n")
            continue
        else:
            break

    # Using a while loop to handle invalid inputs
    while True:
    # Getting the users' input and storing it into a variable while choosing the appropiate object type and transforming it into lower
        day = str(input("\nFilter data by day of week: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.  (Please write full month name)\n").lower())
        print("\nYou've selected: {}\n".format(day.title()))
    # Using a conditional statement to protect the user against unwanted errors
        if day not in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
            print("\nSorry, you'll have to re-write the desired day of the week. Make sure you enter it correctly\n")
            continue
        else:
            break

    print('-'*40)
    # Returns the city, month and day selected by the user
    return city, month, day

# This function loads data from the files
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

    # Loads data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Converts the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracts month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    # Filters by month, if applicable
    if month != 'all':
        # Uses the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filters by month to create the new dataframe
        df = df[df['month'] == month]

    # Filters by day of week if applicable
    if day != 'all':
        # Filters by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    # Returns the dataframe that was created and updated based on filters criteria
    return df

# This function calculates the statistics on the most frequent times of travel
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculates the most common month by using the mode method
    most_common_month = df['month'].mode()[0]
    # This will display the most common month
    print("\nThe number of the most common month is: {}\n".format(most_common_month))

    # Calculates the most common day of the week by using the mode method
    most_common_day = df['day'].mode()[0]
    # This will display the most common day of week
    print("\n{} is the most common day\n".format(most_common_day))

    # First, we have to create a new column containing only the hour out of Start Time column
    df['hour'] = df['Start Time'].dt.hour
    # Calculates the most common hour by using the mode method
    most_common_hour = df['hour'].mode()[0]
    # This will display the most common start hour
    print("\n{} is the most common start hour (time format: from 0 to 24)\n".format(most_common_hour))

    # This will display the amount of time elapsed while doing these computations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This function calculates the statistics about the stations
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculates the most common start station by using the mode method
    most_common_start_station = df['Start Station'].mode()[0]
    # This will display the most commonly used start station
    print("\n{} is the most commonly used start station\n".format(most_common_start_station))

    # Calculates the most common end station by using the mode method
    most_common_end_station = df['End Station'].mode()[0]
    # This will display the most commonly used end station
    print("\n{} is the most commonly used end station\n".format(most_common_end_station))

    # Calculates the most common station combination by using the mode method and by concatenation
    most_common_combination_station = (df['Start Station'].str.cat(df['End Station'], sep=' -> ')).mode()[0]
    # This will display most frequent combination of start station and end station trip
    print("\n{} is the most frequent combination of start station and end station trip\n".format(most_common_combination_station))

    # This will display the amount of time elapsed while doing these computations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This function calculates statistics for trip durations
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculates the total travel time by using the sum method
    total_travel_time = sum(df['Trip Duration'])

    # Converts the total travel time from seconds to seconds, minutes and hours
    m, s = divmod(total_travel_time, 60)
    h, m = divmod(m, 60)
    print("\nThe total travel time is {} h, {} min, {} s.\n".format(h,m,s))

    # Calculates the travel times' mean and converts it into an int
    mean_travel_time = int(round(df['Trip Duration'].mean()))
    mins, sec = divmod(mean_travel_time, 60)

    # Using conditional statements to make the output more user friendly
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print("\nThe average travel time is {} h, {} min, {} s.\n".format(hrs, mins, sec))
    else:
        print("\nThe average travel time is {} min, {} s.\n".format(mins, sec))

    # This will display the amount of time elapsed while doing these computations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This function calculates statistics related to the user
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Using value_counts method to find out the number of counts for each user type
    user_type_counts = df['User Type'].value_counts()
    # This will display counts of user types
    print("\nThe number of user types are: \n{}\n".format(user_type_counts.to_string()))


    # I decided to handle exceptions with a try clause because sometimes there is no gender data
    try:
        user_gender_counts = df['Gender'].value_counts()
    # This will display counts of user gender (M/F)
        print("\nThe number gender counts are: \n{}\n".format(user_gender_counts.to_string()))
    except:
        print("\nSorry, there is no data about the users' gender based on your filters.\n")

    try:
    # The year data was outputed as float so I decided to convert it into int
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("\nThe earliest birth year is: {}\n".format(earliest_birth_year))
        print("\nThe most recent birth year is: {}\n".format(most_recent_birth_year))
        print("\nThe most common birth year is: {}\n".format(most_common_birth_year))
    # Getting errors because the lack of data when the user selected some filters so I decided to use a exception block
    except:
        print("\nSorry, there is no data about the birth year based on your filters.\n")

    # This will display the amount of time elapsed while doing these computations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This function takes the dataframe as an arg and displays 5 rows of raw data, 5 at a time
def raw_data(df):
    """Prompts users if they want to see raw data and renders it."""

    start_time = time.time()
    # Declaring two variables that will be very useful a bit later
    i = 0
    j = 5
    # Using a while loop for control flow
    while True:
    # Getting input from the user whether he/she wants 5 rows of raw data or not
        view_raw = input("\nDo you want to see raw data? (5 rows at a time)\nAnswer with yes or no.\n").lower()
        if view_raw != 'yes':
            break
        else:
    #Using .iloc to ensure we'll output exactly 5 rows, one batch after another
            print(df.iloc[i:j])
            i += 5
            j += 5

    # This will display the amount of time elapsed while doing these computations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This function is the main function and its purpose is to call the other functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

    # The user is asked if he/she would like to start again
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
