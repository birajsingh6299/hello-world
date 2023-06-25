import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('C:/Users/singh/Downloads/journey_data_revised.csv')

# Convert the 'jrdt_local_start_date' column to datetime format with the appropriate format specifier
data['jrdt_local_start_date'] = pd.to_datetime(data['jrdt_local_start_date'], format='%d/%m/%Y')

# Extract the weekday from the 'jrdt_local_start_date' column
data['weekday'] = data['jrdt_local_start_date'].dt.strftime('%A')

# Count the number of journeys for each weekday
journey_counts = data['weekday'].value_counts().sort_values(ascending=False)

# Plotting the bar graph
plt.bar(journey_counts.index, journey_counts.values, width=0.65)

# Adding labels and title
plt.xlabel('Weekday')
plt.ylabel('Number of Journeys')
plt.title('Total Number of Journeys on a Weekday Basis')

# Displaying the total number of journeys on the bars
for i, v in enumerate(journey_counts.values):
    plt.text(i, v + 1, str(v), ha='center')

# Rotating the x-axis labels for better visibility
plt.xticks(rotation=45)

# Display the plot
plt.show()
