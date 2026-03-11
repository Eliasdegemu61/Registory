import pandas as pd
import requests

def convert_json_to_csv():
    url = "https://raw.githubusercontent.com/Eliasdegemu61/Sodex-Tracker-new-v1/refs/heads/main/registry.json"
    
    # Fetch the data
    response = requests.get(url)
    data = response.json()
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Reorder columns to match your request: address, userId
    df = df[['address', 'userId']]
    
    # Save to CSV
    df.to_csv('registry.csv', index=False)
    print("Conversion complete: registry.csv created.")

if __name__ == "__main__":
    convert_json_to_csv()
