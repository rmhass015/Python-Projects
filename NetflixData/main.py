#%%matplotlib inline
import pandas as pd # used to analyze datasets
import matplotlib

df = pd.read_csv("ViewingActivity-Sample.csv")

df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df['Duration'] = pd.to_timedelta(df['Duration'])
df = df.set_index('Start Time')
df.index = df.index.tz_convert('US/Eastern')
df = df.reset_index()

# create a new dataframe called office that that takes from df
# only the rows in which the Title column contains 'The Office (U.S.)'
office = df[df['Title'].str.contains('The Office (U.S.)', regex=False)]

# check for duration of Office watched
office = office[(office['Duration'] > '0 days 00:01:00')]

#Check for weekday of data
office['weekday'] = office['Start Time'].dt.weekday

#check for hour of data
office['hour'] = office['Start Time'].dt.hour

# set our categorical and define the order so the days are plotted Mon - Sun
office['weekday'] = pd.Categorical(office['weekday'], categories=
                                   [0,1,2,4,5,6],
                                   ordered=True)

# create office_by_day andf count the rows for each weeday, assinging the result to that variable
office_by_day = office['weekday'].value_counts()

# sort the index using our categorical, so that Monday (0) is first, Tuesday (1), etc...
office_by_day = office_by_day.sort_index()

# optional: update the font size to make it a bit larger and easier to read
matplotlib.rcParams.update({'font.size': 22})

# plot office_by_day as a bar chart with the listed size and title
office_by_day.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Day')

## NOW TO SET BY HOUR
# set our cateforical and define the order so the hours are plotted 0-23
office['hour'] = pd.Categorical(office['hour'], categories=
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    ordered=True)

# create office_by_hour and count the rows for each hour, assigning the result to that variable
office_by_hour = office['hour'].value_counts()

# sort the index using our categorical, so that midnight (0) is first, 1 a.m. (1) is second, etc.
office_by_hour = office_by_hour.sort_index()

# plot office_by_hour as a bar chart with the listed size and title
office_by_hour.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Hour')

#testing data
print(office.head(1))
# %%
