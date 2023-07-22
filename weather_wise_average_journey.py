import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('C:/Users/singh/OneDrive/Documents/Richa/Data/Final_Journey_Data.csv')

# Group the data by weather condition and count the number of journeys per day
journeys_per_day = data.groupby(['weather', 'jrdt_local_start_date']).size().reset_index(name='number_of_journeys')

# Calculate the average number of journeys per day for each weather condition
average_journeys = journeys_per_day.groupby('weather')['number_of_journeys'].mean()

# Sort the average journeys in descending order
average_journeys = average_journeys.sort_values(ascending=False)

# Plot the bar graph
plt.bar(average_journeys.index, average_journeys.values)

# Add labels and title
plt.xlabel('Weather Condition')
plt.ylabel('Average Number of Journeys per Day')
plt.title('Average Number of Journeys per Day for Each Weather Condition')

for i, v in enumerate(average_journeys.values):
    plt.text(i, v + 1, "{:.2f}".format(v), ha='center')

# Show the plot
plt.show()
