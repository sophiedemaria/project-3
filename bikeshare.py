import time
import pandas as pd
import numpy as np
import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def raw_data():
    city_dict = { 'chicago': pd.read_csv('chicago.csv'),
              'new york city': pd.read_csv('new_york_city.csv'),
              'washington': pd.read_csv('washington.csv') }

    c_df = pd.DataFrame(city_dict['chicago'])
    c_df['City'] = 'chicago'
    n_df = pd.DataFrame(city_dict['new york city'])
    n_df['City'] = 'new york city'
    w_df = pd.DataFrame(city_dict['washington'])
    w_df['City'] = 'washington'
    cn_df = c_df.append(n_df)
    df_raw_data = cn_df.append(w_df)
    return df_raw_data.head(10)


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # get user input for city (chicago, new york city, washington).
    cities = ('chicago', 'new york city', 'washington')
    no = ['no']
    while True:
        city = input('Choose a city: Chicago, New York or Washington?\n> ').lower()
        if city in cities:
            break
        elif city == 'new york':
            city += ' city'
            break
        else:
            picture_2 =' ✘  Oops! ✘ \n'
            print(picture_2  + 'No data for that city. Try again.')
    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    no = ['no']
    while True:
        month = input('Filter by month? If yes, enter a month from January to June, otherwise enter No: \n> {} \n>'.format(months)).lower()
        if month in months:
            break
        elif month in no:
            months = 'all'
            break
        else:
            picture_2 =' ✘  Oops! ✘ \n'
            print(picture_2  + 'invalid entry. Try again.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    no = ['no']
    while True:
        day = input('Filter by day? If yes, enter name of day, otherwise enter No: \n> ').lower()
        if day in days:
            break
        elif day in no:
            days = 'all'
            break
        else:
            picture_2 =' ✘  Oops! ✘ \n'
            print(picture_2  + 'Invalid entry. Try again.')
    picture_3 =' -------- __@      __@       __@       __@      __~@\n ----- _`\<,_    _`\<,_    _`\<,_     _`\<,_    _`\<,_\n ---- (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    print('-'*40, '\n', picture_3, '\n', '\33[95m' + '....Getting Data....' + '\33[0m', '\n', '_'*40)
    if month == 'no' and day == 'no':
        return city, months, days
    elif month == 'no' and day != 'no':
        return city, months, day
    elif month != 'no' and day == 'no':
        return city, month, days
    else:
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
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df, city, month, day):

    """Displays statistics on the most frequent times of travel."""

    picture_3 =' -------- __@      __@       __@       __@      __~@\n ----- _`\<,_    _`\<,_    _`\<,_     _`\<,_    _`\<,_\n ---- (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    print('-'*40, '\n', picture_3, '\n', '\33[95m' + '...Calculating The Most Frequent Times Of Travel...' + '\33[0m', '\n', '_'*40)
    start_time = time.time()
    print('Filtered by City: ' + '\33[92m' + city.title() + '\33[0m' + ' Month: ' + '\33[92m' + month.title() + '\33[0m' + ' Day: ' + '\33[92m' + day.title() + '\33[0m')
    # display the most common month
    if month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        popular_month = df['month'].mode()[0]
    else:
        popular_month = 'Cannot display, as data already filtered by {}'.format(month.title())
    print('The most popular month is: \n{} (January=1)'.format(popular_month))

    # display the most common day of week
    if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        popular_day = df['day'].mode()[0]
    else:
        popular_day = 'Cannot display, as data already filtered by {}'.format(day.title())
    print('The most popular day is: \n{}'.format(popular_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour is:\n{} (24/hr)'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df, city, month, day):

    """Displays statistics on the most popular stations and trip."""''

    picture_3 =' -------- __@      __@       __@       __@      __~@\n ----- _`\<,_    _`\<,_    _`\<,_     _`\<,_    _`\<,_\n ---- (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    print('-'*40, '\n', picture_3, '\n', '\33[95m' + '...Calculating The Most Popular Stations and Trip...' + '\33[0m', '\n', '_'*40)
    start_time = time.time()
    print('Filtered by City: ' + '\33[92m' + city.title() + '\33[0m' + ' Month: ' + '\33[92m' + month.title() + '\33[0m' + ' Day: ' + '\33[92m' + day.title() + '\33[0m')
    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station:\n{}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station:\n{}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    df['Trip'] = 'From' + ' ' + df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
    print('The most frequent trip was:\n{}'.format(df['Trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df, city, month, day):

    """Displays statistics on the total and average trip duration."""

    picture_3 =' -------- __@      __@       __@       __@      __~@\n ----- _`\<,_    _`\<,_    _`\<,_     _`\<,_    _`\<,_\n ---- (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    print('-'*40, '\n', picture_3, '\n', '\33[95m' + '...Calculating Trip Duration...' + '\33[0m', '\n', '_'*40)
    start_time = time.time()
    print('Filtered by City: ' + '\33[92m' + city.title() + '\33[0m' + ' Month: ' + '\33[92m' + month.title() + '\33[0m' + ' Day: ' + '\33[92m' + day.title() + '\33[0m')

    # display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Trip Duration'] = (df['End Time'] - df['Start Time']).abs()  / np.timedelta64(1, 'D')
    df['Trip Duration'] = df['Trip Duration']*86400
    total_duration = df['Trip Duration'].sum()
    total_duration_mins = total_duration//60
    print('Total duration for all trips:\n{} seconds, or {} minutes'.format(total_duration, total_duration_mins))

    # display mean travel time
    average_duration = df['Trip Duration'].mean()
    average_duration_mins = average_duration//60
    print('Average trip duration:\n{} seconds, or {} minutes'.format(average_duration, average_duration_mins))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city, month, day):

    """Displays statistics on bikeshare users."""

    picture_3 =' -------- __@      __@       __@       __@      __~@\n ----- _`\<,_    _`\<,_    _`\<,_     _`\<,_    _`\<,_\n ---- (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    print('-'*40, '\n', picture_3, '\n', '\33[95m' + '...Calculating User Stats...' + '\33[0m', '\n', '_'*40)
    start_time = time.time()
    print('Filtered by City: ' + '\33[92m' + city.title() + '\33[0m' + ' Month: ' + '\33[92m' + month.title() + '\33[0m' + ' Day: ' + '\33[92m' + day.title() + '\33[0m')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('The data includes the below user types and the count for each:\n{}'. format(count_user_types))
    # Display counts of gender
    if city == 'washington':
        print('No gender data to display for city: Washington')
    else:
        count_gender = df['Gender'].value_counts()
        print('The count for each gender:\n{}'.format(count_gender))

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('The eldest user was born in {}\nThe youngest user was born in {}\nMost common birth year: {}'.format(int(earliest_year), int(recent_year), int(common_year)))
    else:
        print('No birth year data to display for city: Washington')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        picture_1="   ,--.      <__)\n   `- |________7\n      |`.      |\n   .--|. \     |.\--.\n  /   j \ `.7__j__\  \ \n |   o   | (o)____O)  |\n  \     /   J  \     /\n   `---'        `---' \n"

        print(picture_1)
        print('\33[92m' + 'Hello! Let\'s explore some US bikeshare data!' + '\33[0m')
        Question = input('Select Number. Would you like to:\n1 - Preview Raw Data\n2 - Apply a Filter and Get Summaries:\n')
        if Question == '1':
            print('Loading Raw Data......')
            print(raw_data())
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        elif Question == '2':
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df, city, month, day)
            next_q = input('Next: Station Stats. Press any key/enter to continue:\n')
            station_stats(df, city, month, day)
            next_q1 = input('Next: Trip Stats. Press any key/enter to continue:\n')
            trip_duration_stats(df, city, month, day)
            next_q2 = input('Next: User Stats. Press any key/enter to continue:\n')
            user_stats(df, city, month, day)
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
