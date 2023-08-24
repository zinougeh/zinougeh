import requests
import csv

# Define the API endpoint URL
api_url = "https://jsonplaceholder.typicode.com/posts"

# Fetch data from the API
response = requests.get(api_url)
data = response.json()

# Specify the CSV file path
csv_file_path = "posts.csv"

# Extract keys from the first record to use as CSV headers
if data and isinstance(data, list):
    csv_headers = data[0].keys()
else:
    print("No data or invalid response.")
    exit()

# Write data to the CSV file
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()

    for record in data:
        writer.writerow(record)

print(f"Data has been successfully written to {csv_file_path}.")
