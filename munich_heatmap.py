import pandas as pd
import folium
from folium.plugins import HeatMap

import pandas as pd
import folium
from folium.plugins import HeatMap

# Read the CSV file
data = pd.read_csv('C:/Users/singh/OneDrive/Documents/Richa/Data/journey_data_revised.csv')

# Filter out rows with missing or invalid latitude and longitude values
data = data.dropna(subset=['jrny_start_latitude', 'jrny_start_longitude'])

# Extract the latitude and longitude columns
latitudes = data['jrny_start_latitude']
longitudes = data['jrny_start_longitude']

# Count the number of journeys for each location
journey_count = data.groupby(['jrny_start_latitude', 'jrny_start_longitude']).size().reset_index(name='count')

# Create a list of latitudes, longitudes, and journey count as tuples
locations = list(zip(journey_count['jrny_start_latitude'], journey_count['jrny_start_longitude'], journey_count['count']))

# Create a map centered around Munich
map_munich = folium.Map(location=[48.1351, 11.5820], zoom_start=12)

# Add the HeatMap layer to the map
HeatMap(locations).add_to(map_munich)

# Save the map as an HTML file
map_munich.save('C:/Users/singh/OneDrive/Documents/Richa/Results/munich_map.html')
