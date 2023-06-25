import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file. Enter your file location
data = pd.read_csv('C:/Users/singh/Downloads/journey_data_revised.csv')

# Convert 'jrdt_local_start_datm' column to datetime format
data['jrdt_local_start_datm'] = pd.to_datetime(data['jrdt_local_start_datm'], format='%d/%m/%Y %H:%M')

# Define the strike days
strike_dates = ['02/03/2023', '03/03/2023', '27/03/2023', '19/05/2023']

# Filter the data for strike days
strike_data = data[data['jrdt_local_start_datm'].dt.date.isin(pd.to_datetime(strike_dates, format='%d/%m/%Y').date)]

# Group the strike data by hour range and calculate the average number of journeys
strike_hourly_journeys = strike_data.groupby(strike_data['jrdt_local_start_datm'].dt.hour)['jrdt_local_start_datm'].count()
strike_days_per_hour = strike_data['jrdt_local_start_datm'].dt.date.nunique()
strike_average_journeys = strike_hourly_journeys / strike_days_per_hour
# Plotting the line graph for strike days
plt.plot(strike_average_journeys.index.astype(str), strike_average_journeys.values, label='Strike Days')

# Filter the data for non-strike days
non_strike_data = data[~data['jrdt_local_start_datm'].dt.date.isin(pd.to_datetime(strike_dates, format='%d/%m/%Y').date)]

# Group the non-strike data by hour range and calculate the average number of journeys
non_strike_hourly_journeys = non_strike_data.groupby(non_strike_data['jrdt_local_start_datm'].dt.hour)['jrdt_local_start_datm'].count()
non_strike_days_per_hour = non_strike_data['jrdt_local_start_datm'].dt.date.nunique()
non_strike_average_journeys = non_strike_hourly_journeys / non_strike_days_per_hour
# Plotting the line graph for non-strike days
plt.plot(non_strike_average_journeys.index.astype(str), non_strike_average_journeys.values, label='Non-Strike Days')

# Adding labels and title
plt.xlabel('Hour Range')
plt.ylabel('Average Number of Journeys')
plt.title('Average Hourly Journeys (Strike Days vs Non-Strike Days)')

# Adding legend
plt.legend()

# Display the plot
plt.show()
