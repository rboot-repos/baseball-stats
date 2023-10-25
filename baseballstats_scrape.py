import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape
url = "https://www.baseball-reference.com/leagues/majors/2022-standard-batting.shtml#players_standard_batting"

# Send an HTTP GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract the batting statistics table
table = soup.find('table', {'id': 'standard_batting'})
df = pd.read_html(str(table))[0]

# Clean the data (e.g., remove rows with missing values)
df.dropna(inplace=True)

# Save the data to a CSV file for further analysis
df.to_csv('mlb_batting_stats_2022.csv', index=False)
