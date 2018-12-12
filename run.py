from bike_functions import *


day_list = {"sunday": "6", "monday": "0", "tuesday": "1", "wednesday": "2", "thursday": "3", "saturday": "5",
            "friday": "4"}
month_list = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6", "none": None}
filter_list = ["month", "day", "none"]
city_list = ["new york", "chicago", "washington"]
raw_list = ["y", "n"]

print('Hello! Let\'s explore some US bikeshare data!')

# get user input for CITY (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
choose_city = str(input("Would you like to see data for Chicago, New York, or Washington?\n")).lower()
while choose_city not in city_list:
    choose_city = str(input("That is not a valid city. Which city would you like to explore?\n")).lower()

# get user input to see 5 lines of raw data
raw_data = str(input("Would you like to see a few lines of raw data before we filter? (Y/N)\n")).lower()
i = 0
j = 5
while raw_data not in raw_list:
    raw_data = str(input("That is not a valid answer. Would you like to see a few lines of raw data? (Y/N)\n")).lower()
while raw_data == 'y':
    #print 5 lines
    #prompt again
    #cap_city = choose_city.capitalize()
    sample_df = pd.read_csv(CITY_DATA[choose_city])
    print(sample_df[i:j])
    i += 5
    j += 5
    print()
    raw_data = str(input("Would you like to see a few more lines? (Y/N)\n")).lower()

# get user input for FILTER (month, day, none)
choose_filter = str(input("Would you like to filter the data by month, day, or not at all? (Type 'none' for no time filter)\n")).lower()
while choose_filter not in filter_list:
    choose_filter = str(input("That is not a valid filter. Month, day, or none?\n")).lower()

# get user input for MONTH (january, february, ... , june)
if choose_filter == "month":
    choose_month = str(input("Which month (January through June)?\n")).lower()
    choose_day = None
    while choose_month not in month_list:
        choose_month = str(input("That is not a valid month. By which month would you like to filter (January through June)?\n")).lower()

# get user input for DAY of WEEK (monday, tuesday, ... sunday)
elif choose_filter == "day":
    choose_day = str(input("Which day of the week (Sunday through Saturday)?\n")).lower()
    choose_month = None
    while choose_day not in day_list:
        choose_day = str(input("That is not a valid day. Pick another. (Sunday through Saturday)\n")).lower()

else:
    choose_month = None
    choose_day = None

print('-'*40)

# save new data frame into variable
new_df = create_csv(choose_city)

# run time statistics using new data frame and filters as inputs
time_stats(new_df, choose_filter, choose_month, choose_day)

# run station statistics using new data frame and filters as inputs
station_stats(new_df, choose_filter, choose_month, choose_day)

# run trip duration statistics
trip_duration_stats(new_df, choose_filter, choose_month, choose_day)

# run user statistics using new data frame and filters as inputs, including city
user_stats(new_df, choose_city, choose_filter, choose_month, choose_day)