import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data = pd.read_csv(r'C:\Users\joema\Downloads\archive (18)\usa_county_wise.csv')

print(data.head(2))

# Define columns of interest
Columns_of_interest = [ 'Confirmed', 'Deaths' ]

provinces = ['Florida', 'California', 'Texas', 'Pennsylvania', 'New York']
total_deaths = []


# Loop through each province and calculate the total confirmed and deaths
for province in provinces:
    province_data = data[data['Province_State'] == province]  # Filter by province
    total_confirmed = province_data['Confirmed'].sum()  # Sum confirmed cases
    deaths_sum = province_data['Deaths'].sum()  # Sum deaths for the province
    total_deaths = province_data['Deaths'].sum()
    

    # Display the results
    print(f"Total Confirmed Cases in {province}: {total_confirmed}")
    print(f"Total Deaths in {province}: {total_deaths}")
    print("-" * 40)  # Add a separator for clarity




# Create the bar graph
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
plt.bar(provinces,total_deaths , color='purple')  # Create a bar graph

# Add labels and title
plt.xlabel('Provinces')  # X-axis label
plt.ylabel('Deaths')      # Y-axis label
plt.title('Total Deaths Per Province')  # Graph title

# Optional: Add gridlines (for better readability)
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Show the graph
plt.tight_layout()  # Adjust layout to avoid clipping of labels
plt.show()