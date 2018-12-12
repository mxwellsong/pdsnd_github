import time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import statistics


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

day_list = {"sunday": "6", "monday": "0", "tuesday": "1", "wednesday": "2", "thursday": "3", "saturday": "5",
            "friday": "4"}
month_list = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6"}
filter_list = ["month", "day", "none"]
city_list = ["new York", "chicago", "washington"]
raw_list = ["Y", "N"]

def create_csv(city):
    # create df
    df = pd.read_csv(CITY_DATA[city])

    # create new start time column
    start_time_col = df['Start Time']
    start_time_col_vals = []
    for i in range(len(df)):
        val = datetime.strptime(start_time_col[i], '%Y-%m-%d %H:%M:%S')
        start_time_col_vals.append(val)
    df['New Start Time'] = start_time_col_vals

    # create new end time column
    end_time_col = df['End Time']
    end_time_col_vals = []
    for i in range(len(df)):
        val = datetime.strptime(end_time_col[i], '%Y-%m-%d %H:%M:%S')
        end_time_col_vals.append(val)
    df['End Time'] = end_time_col_vals

    # create month column
    months = []
    for new_time in df['New Start Time']:
        months.append(new_time.month)
    df['Month'] = months

    # create day of week column
    days = []
    for new_time in df['New Start Time']:
        days.append(new_time.dayofweek)
    df['Day'] = days

    # create hour column
    hours = []
    for new_time in df['New Start Time']:
        hours.append(new_time.hour)
    df['Hour'] = hours

    # create trip column
    trips = []
    for start, end in zip(df['Start Station'], df['End Station']):
        combo = start + " to " + end
        trips.append(combo)
    df['Trip'] = trips

    return df



def time_stats(df, filter, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # if user chose not to filter by month or day
    if filter == "none":
        # find most common month
        common_month = int(df['Month'].mode())
        for month in month_list:
            if month_list[month] == str(common_month):
                disp_month = month
        print(str(disp_month).capitalize() + " is the most popular month.")

        # find most common day of the week
        common_day = int(df['Day'].mode())
        for day in day_list:
            if day_list[day] == str(common_day):
                disp_day = day
        print(str(disp_day).capitalize() + " is the most popular day of the week.")

        # find most common hour of the day
        common_hour = int(df['Hour'].mode())
        print(str(common_hour) + ":00 is the most popular start hour of the day.")

    # if user chose to filter by month
    elif filter == "month":
        # create a new data frame with only the chosen month
        month_df = df[ df['Month'] == int(month_list[month]) ]

        # find most common day given the chosen month
        com_day_given_month = int(month_df['Day'].mode())
        for day in day_list:
            if day_list[day] == str(com_day_given_month):
                disp_day = day
        print(str(disp_day).capitalize() + " is the most popular day of the week in " + str(month).capitalize() + ".")

        # find most common hour of the day given the chosen month
        com_hour_given_month = int(month_df['Hour'].mode())
        print(str(com_hour_given_month) + ":00 is the most popular start hour in " + month.capitalize() + ".")

    # if user chose to filter by day
    else:
        # create a new data frame with only the chosen day of the week
        day_df = df[ df['Day'] == int(day_list[day]) ]

        # find most common month given the chosen day of the week
            # not the most intuitive statistic
        com_month_given_day = int(day_df['Month'].mode())
        for month in month_list:
            if month_list[month] == str(com_month_given_day):
                disp_month = month
                print(str(disp_month).capitalize() + " is the most popular month for " + day.capitalize() + "s.")

        # find most common hour of the day given the chosen day of the week
        com_hour_given_day = int(day_df['Hour'].mode())
        print(str(com_hour_given_day) + ":00 is the most popular start hour on " + day.capitalize() + "s.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def station_stats(df, filter, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # if user chose not to filter by month or day
    if filter == "none":
        # find most common Start Station
        common_start = df['Start Station'].mode()
        print(common_start[0] + " is the most popular start station.")

        # find most common End Station
        common_end = df['End Station'].mode()
        print(common_end[0] + " is the most popular end station.")

        # find most common trip (Start to End combination)
        common_trip = df['Trip'].mode()
        print(common_trip[0] + " is the most popular trip.")

    # if user chose to filter by month
    elif filter == "month":
        # create a new data frame with only the chosen month
        month_df = df[ df['Month'] == int(month_list[month]) ]

        # find most common Start Station given the chosen month
        com_start_given_month = month_df['Start Station'].mode()
        print(com_start_given_month[0] + " is the most popular start station in " + month.capitalize() + ".")

        # find most common End Station given the chosen month
        com_end_given_month = month_df['End Station'].mode()
        print(com_end_given_month[0] + " is the most popular end station in " + month.capitalize() + ".")

        # find most common trip (Start to End combination) given the chosen month
        common_trip_given_month = month_df['Trip'].mode()
        print(common_trip_given_month[0] + " is the most popular trip in " + month.capitalize() + ".")

    # if user chose to filter by day
    else:
        # create a new data frame with only the chosen day of the week
        day_df = df[ df['Day'] == int(day_list[day]) ]

        # find most common Start Station given the chosen day of the week
        com_start_given_day = day_df['Start Station'].mode()
        print(com_start_given_day[0] + " is the most popular start station on " + day.capitalize() + "s.")

        # find the most common End Station given the chosen day of the week
        com_end_given_day = day_df['End Station'].mode()
        print(com_end_given_day[0] + " is the most popular end station on " + day.capitalize() + "s.")

        # find the most common trip (Start to End combination) given the chosen day of the week
        common_trip_given_day = day_df['Trip'].mode()
        print(common_trip_given_day[0] + " is the most popular trip on " + day.capitalize() + "s.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df, filter, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # if user chose not to filter by month or day
    if filter == "none":
        # find total travel time
        travel_time = df['Trip Duration'].sum()
        total_time = timedelta(seconds = travel_time)
        print("The total travel time is " + str(total_time) + ".")

        # find mean travel time
        mean_time = df['Trip Duration'].mean()
        conv_mean = timedelta(seconds = mean_time)
        print("The mean travel time is " + str(conv_mean) + ".")

    # if user chose to filter by month
    elif filter == "month":
        # create a new data frame with only the chosen month
        month_df = df[ df['Month'] == int(month_list[month]) ]

        # find total travel time given the chosen month
        travel_time_given_month = month_df['Trip Duration'].sum()
        total_time_given_month = timedelta(seconds = travel_time_given_month)
        print("The total travel time is " + str(total_time_given_month) + ".")

        # find mean travel time given the chosen month
        mean_time_given_month = month_df['Trip Duration'].mean()
        conv_mean_given_month = timedelta(seconds = mean_time_given_month)
        print("The mean travel time in " + month.capitalize() + " is " + str(conv_mean_given_month) + ".")

    # if user chose to filter by day
    else:
        # create a new data frame with only the chosen day of the week
        day_df = df[ df['Day'] == int(day_list[day]) ]

        # find total travel time given the chosen day of the week
        travel_time_given_day = day_df['Trip Duration'].sum()
        total_time_given_day = timedelta(seconds = travel_time_given_day)
        print("The total travel time is " + str(total_time_given_day) + ".")

        # find mean travel time given the chosen day of the week
        mean_time_given_day = day_df['Trip Duration'].mean()
        conv_mean_given_day = timedelta(seconds = mean_time_given_day)
        print("The mean travel time on " + day.capitalize() + "s is " + str(conv_mean_given_day) + ".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df, city, filter, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # if user chose not to filter by month or day
    if filter == "none":
        # count different values of User Type
        user_count = df['User Type'].value_counts()
        sub_count = user_count['Subscriber']
        cust_count = user_count['Customer']
        print("Subscribers: " + str(sub_count))
        print("Customers: " + str(cust_count))
        print()

        # since Washington does not have Gender or Birth Year columns...
        if city != "washington":
            # count different values of Gender
            gender_count = df['Gender'].value_counts()
            male_count = gender_count['Male']
            female_count = gender_count['Female']
            print("Men: " + str(male_count))
            print("Women: " + str(female_count))
            print()

            # earliest, most recent, and most common years of birth
            early_birth = int(df['Birth Year'].min())
            rec_birth = int(df['Birth Year'].max())
            com_birth = int(df['Birth Year'].mode())
            print("Earliest Year of Birth: " + str(early_birth))
            print("Most Recent Year of Birth: " + str(rec_birth))
            print("Most Common Year of Birth: " + str(com_birth))

    elif filter == "month":
        # create a new data frame with only the chosen month
        month_df = df[ df['Month'] == int(month_list[month]) ]

        # count different values of User Type
        user_count = month_df['User Type'].value_counts()
        sub_count = user_count['Subscriber']
        cust_count = user_count['Customer']
        print("Subscribers in " + month.capitalize() + ": " + str(sub_count))
        print("Customers in " + month.capitalize() + ": " + str(cust_count))
        print()

        # since Washington does not have Gender or Birth Year columns...
        if city != "washington":
            # count different values of Gender
            gender_count = month_df['Gender'].value_counts()
            male_count = gender_count['Male']
            female_count = gender_count['Female']
            print("Men in " + month.capitalize() + ": " + str(male_count))
            print("Women in " + month.capitalize() + ": " + str(female_count))
            print()

            # earliest, most recent, and most common years of birth
            early_birth_given_day = int(month_df['Birth Year'].min())
            rec_birth_given_day = int(month_df['Birth Year'].max())
            com_birth_given_day = int(month_df['Birth Year'].mode())
            print("Earliest Year of Birth (" + month.capitalize() + "): " + str(early_birth_given_day))
            print("Most Recent Year of Birth (" + month.capitalize() + "): " + str(rec_birth_given_day))
            print("Most Common Year of Birth (" + month.capitalize() + "): " + str(com_birth_given_day))

    else:
        # create a new data frame with only the chosen day of the week
        day_df = df[ df['Day'] == int(day_list[day]) ]

        # count different values of User Type
        user_count_given_day = day_df['User Type'].value_counts()
        sub_count_given_day = user_count_given_day['Subscriber']
        cust_count_given_day = user_count_given_day['Customer']
        print("Subscribers over all " + day.capitalize() + "s: " + str(sub_count_given_day))
        print("Customers over all " + day.capitalize() + "s: " + str(cust_count_given_day))
        print()

        # since Washington does not have Gender or Birth Year columns...
        if city != "washington":
            # count different values of Gender
            gender_count_given_day = day_df['Gender'].value_counts()
            male_count_given_day = gender_count_given_day['Male']
            female_count_given_day = gender_count_given_day['Female']
            print("Men over all " + day.capitalize() + "s: " + str(male_count_given_day))
            print("Women over all " + day.capitalize() + "s: " + str(female_count_given_day))
            print()

            # earliest, most recent, and most common years of birth
            early_birth_given_day = int(day_df['Birth Year'].min())
            rec_birth_given_day = int(day_df['Birth Year'].max())
            com_birth_given_day = int(day_df['Birth Year'].mode())
            print("Earliest Year of Birth (" + day.capitalize() + "s): " + str(early_birth_given_day))
            print("Most Recent Year of Birth (" + day.capitalize() + "s): " + str(rec_birth_given_day))
            print("Most Common Year of Birth (" + day.capitalize() + "s): " + str(com_birth_given_day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


