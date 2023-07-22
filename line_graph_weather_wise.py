import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('C:/Users/singh/OneDrive/Documents/Richa/Data/Final_Journey_Data.csv')

# Group the data by weather condition and hour, and calculate the average hourly journeys
average_hourly_journeys = data.groupby(['weather', 'hour']).size().reset_index(name='average_journeys')

# Calculate the total number of unique days for each weather condition
unique_days_per_weather = data.groupby('weather')['jrdt_local_start_date'].nunique().reset_index(name='unique_days')

# Merge the two DataFrames to include the unique days per weather condition in the average_hourly_journeys DataFrame
average_hourly_journeys = pd.merge(average_hourly_journeys, unique_days_per_weather, on='weather')

# Calculate the average count of journeys per hour for each weather condition
average_hourly_journeys['average_journeys_per_hour'] = average_hourly_journeys['average_journeys'] / average_hourly_journeys['unique_days']

# Plot the line graph
for weather_condition, group_data in average_hourly_journeys.groupby('weather'):
    plt.plot(group_data['hour'], group_data['average_journeys_per_hour'], label=weather_condition)

# Add labels and title
plt.xlabel('Hour')
plt.ylabel('Average Hourly Journeys')
plt.title('Average Hourly Journeys for Each Weather Condition')
plt.legend()

# Show the plot
plt.show()
