import requests
import pandas as pd

url = "https://data.niwa.co.nz/api/observations"  # Placeholder URL

params = {
    'station': 'AUCKLAND_ID',  # Replace with actual station ID
    'parameter': 'TMean',
    'start_date': '2024-01-01',
    'end_date': '2024-12-31',
    'frequency': 'monthly',
    'format': 'json'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    try:
        data = response.json()
        print(data)  # or convert to DataFrame
    except ValueError:
        print("Response is not valid JSON:")
        print(response.text)
else:
    print(f"Failed to fetch data: {response.status_code}")
    print("Response content:", response.text)
