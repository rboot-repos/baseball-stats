# Load the data from the CSV file
df = pd.read_csv('mlb_batting_stats_2022.csv')

# Calculate descriptive statistics
summary_stats = df.describe()

# Calculate the average batting average (BA)
average_ba = df['BA'].mean()

# Filter the data to find the players with the highest home run (HR) count
top_homerun_hitters = df.nlargest(10, 'HR')

# Calculate the correlation between home runs and RBIs
correlation = df['HR'].corr(df['RBI'])
