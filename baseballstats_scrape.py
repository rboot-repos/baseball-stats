import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.baseball-reference.com/leagues/majors/2022-standard-batting.shtml#players_standard_batting"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'id': 'standard_batting'})
df = pd.read_html(str(table))[0]

df.dropna(inplace=True)

df.to_csv('mlb_batting_stats_2022.csv', index=False)
