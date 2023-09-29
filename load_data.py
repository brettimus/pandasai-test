import pandas as pd
import json

def load_dataframe():
  # Open the JSON file
  with open('./data.json', 'r') as f:
      # Load the JSON data into a Python object
      data = json.load(f)

  if data:
      # Initialize a list to hold the data points
      data_points = []

      # Extract time series data from response
      for series in data['data']['result']:
          metric_function = series['metric'].get('function', 'unknown')  # Replace with desired metric function if needed
          metric_module = series['metric'].get('module', 'unknown')  # Replace with desired metric module if needed
          # metric_service = series['metric'].get('service_name', 'unknown')  # Replace with desired metric service if needed
          metric_name = f"{metric_module}.{metric_function}"
          for timestamp, value in series['values']:
              data_points.append({
                  'timestamp': pd.to_datetime(timestamp, unit='s'),  # Convert timestamp to datetime
                  'metric': metric_name,
                  'value': float(value)  # Convert value to float
              })

      # Create DataFrame
      return pd.DataFrame(data_points)