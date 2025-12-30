
# Example of accessing the integrated platform's API for real-time data
import requests

# Endpoint for real-time public transportation data
transportation_url = "https://api.smartcity.ae/public_transportation"
# Endpoint for healthcare facility utilization data
healthcare_url = "https://api.smartcity.ae/healthcare_utilization"

# Fetch real-time transportation data
transportation_response = requests.get(transportation_url)
if transportation_response.status_code == 200:
    transportation_data = transportation_response.json()
    print("Real-Time Public Transportation Data:", transportation_data)
else:
    print("Failed to retrieve transportation data")

# Fetch healthcare facility utilization data
healthcare_response = requests.get(healthcare_url)
if healthcare_response.status_code == 200:
    healthcare_data = healthcare_response.json()
    print("Healthcare Facility Utilization Data:", healthcare_data)
else:
    print("Failed to retrieve healthcare data")

# Example of combining data for analysis
# Here we just print the first entry from each dataset to demonstrate
if transportation_data and healthcare_data:
    print("Combined Data Analysis Example:")
    print("First Bus Location:", transportation_data['buses'][0])
    print("First Healthcare Facility Utilization:", healthcare_data['facilities'][0])
