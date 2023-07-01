import pandas as pd

# Read the CSV file
data = pd.read_csv('C:/Users/singh/OneDrive/Documents/Richa/Data/journey_data_revised.csv')

# Convert 'jrdt_local_start_datm' column to datetime format
data['jrdt_local_start_datm'] = pd.to_datetime(data['jrdt_local_start_datm'], format='%d/%m/%Y %H:%M')

# Group the data hourly and calculate the average distance, average journey duration, and average count of journeys
hourly_data = data.groupby(data['jrdt_local_start_datm'].dt.hour).agg({
    'jrdt_driven_km': 'mean',
    'jrdt_journey_duration_minutes': 'mean',
    'jrdt_local_start_datm': lambda x: len(x) / x.dt.date.nunique()  # Calculate average count
}).rename(columns={'jrdt_local_start_datm': 'average_journey_count'})


# Save the resultant table as a CSV file
hourly_data.to_csv('C:/Users/singh/OneDrive/Documents/Richa/Results/hourly_data_output.csv', index=True)

# Confirm that the CSV file has been saved
# print(hourly_data)
print('done')
